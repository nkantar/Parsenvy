import setuptools

from parsenvy import (
    __author__,
    __author_email__,
    __description__,
    __name__,
    __url__,
    __version__,
)

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=__name__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url=__url__,
    packages=setuptools.find_packages(),
)
