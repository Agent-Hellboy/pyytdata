import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pyytdata",
    author="Prince Roshan",
    author_email="princekrroshan01@gmail.com",
    url="https://github.com/princekrroshan01/youtube-api-wrapper",
    description=("A python library which provides all possible metadata of YouTube videos."),
    long_description=read("README.rst"),
    license="MIT",
    packages=["pyytdata", "pyytdata.util"],
    keywords=[
        "youtube-api" "recommend-youtube-videos",
        "youtube-data",
        "python",
        "wrapper",
        "youtube-data-api-v3",
        "youtube-api-wrapper",
        "youtube-api-v3",
    ],
    python_requires=">=3.7",
    install_requires=["google-api-python-client"],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
