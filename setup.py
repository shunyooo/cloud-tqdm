from setuptools import setup


readme = ""
with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="cloud-tqdm",
    version='0.0.1',
    description="Visualize the progress of a Python script on the web.",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords=["progress", "tqdm", "cloud"],
    author="shunyooo",
    author_email="shunyo.kawamoto@gmail.com",
    license="Apache License 2.0",
    packages=[
        "cloud_tqdm",
    ],
    url='https://github.com/shunyooo/cloud-tqdm',
    install_requires=[
        "tqdm"
    ],
)