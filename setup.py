#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup


INSTALL_REQUIRES = []

setup(
    name='emqx_sdk',
    version='0.1',
    author='emqx',
    author_email='taodk@emqx.io',
    url='https://github.com/emqx-extension-python-sdk',
    description='The Python SDK for emqx-extension-hook',
    long_description=open("README.rst").read(),
    platforms=['any'],
    license='Apache License 2.0',
    install_requires=INSTALL_REQUIRES,
    python_requires='>=3.6.0',
    keywords=[
        'emqx',
    ]
)