#!/usr/bin/env python

## this code was from https://docs.python.org/3/distutils/setupscript.html
#from distutils.core import setup
#
#setup(name='funniest',
      #version='1.0',
      #description='Funniest joke in the world',
      #author='mark regine',
      #author_email='mregine@betaxanalytics.com',
      #url='http://github.com/markregine/funniest/',
      #packages=['funniest'],
     #)

## this code from https://packaging.python.org/tutorials/packaging-projects/
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="funniest-markregine",
    version="0.0.1",
    author="mark regine",
    author_email="mregine@betaxanalytics.com",
    description="Funniest joke in the world",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/markregine/funniest/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows 10",
    ],
)