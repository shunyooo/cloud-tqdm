import tqdm
import requests
import json
import threading
from time import time
import inspect
from .constants import BASE_URL, APP_URL, POST_INTERVAL_SEC, Status
from IPython import get_ipython

def is_notebook():
    ipython = get_ipython()
    return ipython is not None and ipython.has_trait('kernel') is not None

def post_data(data):
    q = '&'.join([f'{key}={value}' for key, value in data.items()])
    url = f'{BASE_URL}?{q}'
    res = requests.get(url)
    return json.loads(res.text).get('res')

class cloud_tqdm(tqdm.tqdm):
    """
    Implementation of tqdm that can be displayed on the web.
    """
    @property
    def should_post(self):
        is_past = self.last_post_time is None \
                  or (time() - self.last_post_time) > POST_INTERVAL_SEC
        return not self.loading and is_past
    
    def post_if_need(self, force):
        if self.should_post or force:
            self.loading = True
            try:
                res = post_data({
                    'total': self.total,
                    'description': self.desc,
                    'value': self.n,
                    'status': self.status,
                    'progress_id': self.pid,
                })
            except Exception as e:
                print(e)
            self.last_post_time = time()
            self.loading = False

    def display(self, msg=None, pos=None, status=None):
        # TODO: 継承元tqdmの表示をだせるように
        #       なぜか出力がprint的になってしまう
        # super().display(msg, pos)
        force = status is not None
        self.status = Status.doing if status is None else status
        threading.Thread(name='post_if_need', target=self.post_if_need, args=[force]).start()

    def print_link(self):
        if is_notebook():
            # if jupyter
            # from IPython.core.display import HTML, display
            # display(HTML(f'cloud-tqdm → <a href="{self.url}">{self.url}</a>'))
            print(f'cloud-tqdm → {self.url}')
        else:
            print(f'cloud-tqdm → {self.url}')

    def __init__(self, *args, **kwargs):
        try:
            res = post_data(dict({
                'total': 0,
                'description': 'Initialized',
                'value': 0,
                'status': 'init',
            }))
            self.pid = res.get('progress_id')
            self.last_post_time = None
            self.loading = False
            self.status = 'init'
            self.url = f'{APP_URL}?pid={self.pid}'
            self.print_link()
        except:
            raise Exception('failed cloud-tqdm init')
        
        super().__init__(*args, **kwargs)
        self.sp = self.display

    def __iter__(self, *args, **kwargs):
        try:
            for obj in super().__iter__(*args, **kwargs):
                yield obj
        except:
            self.display(status=Status.cancel)
            raise

    def update(self, *args, **kwargs):
        try:
            super().update(*args, **kwargs)
        except:
            self.display(status=Status.cancel)
            raise
            
    def close(self, *args, **kwargs):
        super().close(*args, **kwargs)
        if self.total and self.n < self.total:
            self.display(status=Status.cancel)
        else:
            if self.leave:
                self.display(status=Status.success)
            else:
                self.display(status=Status.done)
