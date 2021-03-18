#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import path

from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='aiogram-logging',
    description='Simplifies sending logs from your bots to DB.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='0.0.1',
    url='https://github.com/dkeysil/aiogram-logging',
    author='Dmitry Keysil',
    author_email='kl0opa.11@gmail.com',
    license='MIT',
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(include=['aiogram_logging', 'aiogram_logging.*']),
    install_requires=[
        'aiogram<3',
        'aioinflux',
    ],
    python_requires=">=3.6",
)