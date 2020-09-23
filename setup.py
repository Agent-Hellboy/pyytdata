import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pyytdata",
    version="0.2.2",
    author="Prince Roshan",
    author_email="princekrroshan01@gmail.com",
    url="https://github.com/princekrroshan01/youtube-api-wrapper",
    description=("this is a simple client for youtube data api v3"),
    long_description=read("README.rst"),
    license="MIT",
    packages=['pyytdata', 'pyytdata.util'],
    keywords=[
        "youtube-api" "recommend-youtube-videos",
        "youtube-data",
        "python",
        "wrapper",
        "youtube-data-api-v3",
        "youtube-api-wrapper",
        "youtube-api-v3",
    ],
    python_requires=">=3.6",
    install_requires=["google-api-python-client"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
