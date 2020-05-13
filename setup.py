import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pyytdata",
    version="0.0.8",
    author="Prince Roshan",
    author_email="princekrroshan01@gmail.com",
    url="https://github.com/princekrroshan01/youtube-api-wrapper",
    description=("this is a simple client for youtube data api v3"),
    long_description=read("README.md"),
    license="MIT",
    py_modules=["pyytdata/pyytdata"],
    install_requires=["google-api-python-client"],
    include_package_data=True,
)
