![cloud-tqdm](https://user-images.githubusercontent.com/17490886/86932197-fdb32f80-c173-11ea-99e8-d9300811f5bb.png)

[![PyPI version](https://badge.fury.io/py/cloud-tqdm.svg)](https://badge.fury.io/py/cloud-tqdm)


`cloud-tqdm` visualize the progress of a Python script on the web.

`cloud-tqdm` inherits from [tqdm](https://github.com/tqdm/tqdm), so it can be run in the same way as tqdm.



![output](https://user-images.githubusercontent.com/17490886/86999508-b7021b80-c1ed-11ea-8332-c9bde4798667.gif)



## Installation

```bash
pip install cloud-tqdm
```



## Usage

Visualize the progress of a Python script on the web.

```python
import time
from cloud_tqdm import cloud_tqdm

for i in cloud_tqdm(range(30), desc="Processing"):
    print(i)
    time.sleep(1)
    
cloud-tqdm → https://cloud-tqdm....
1
2
3
```

![image-20200709142048295](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggkngho7xzj321u0eygn7.jpg)



Multiple progresses can be displayed on the same page by connecting `pid` with URLs.


```bash
https://cloud-tqdm.web.app/progress?pid=-MBm07wc3HJ-JZfeOc5a&pid=-MBm0JSG-NQ6HswT81Ru&pid=-MBm0Qyc8lIbWzfArUYw
```

![image-20200709142539326](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggknlhkbelj31jr0u0wja.jpg)



## Related repositories

- [cloud-tqdm-api](https://github.com/shunyooo/cloud-tqdm-api)
- [cloud-tqdm-app](https://github.com/shunyooo/cloud-tqdm-app)



## Future

- Do not interfere with existing progress displays.
- Implements of Test.
- Grouping of progress by user or device.

- Publish URLs that group progress by user or device.
- Discard the progress from the DB when a certain amount of time has passed since the last update.

