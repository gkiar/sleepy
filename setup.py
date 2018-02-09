# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "sleepy"
VERSION = "0.1.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Sleepy",
    author_email="",
    url="",
    keywords=["Swagger", "Sleepy"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['sleepy=sleepy.__main__:main']},
    long_description="""\
    Sleepy is a RESTful querying server for your arbitrary datasets and types. 
    """
)

