#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup


INSTALL_REQUIRES = []

setup(
    name='emqx-extension-sdk',
    version='0.1',
    author='emqx',
    author_email='taodk@emqx.io',
    url='https://github.com/emqx/emqx-python-sdk',
    description='The Python SDK For EMQ X Extension',
    long_description=open("README.rst").read(),
    platforms=['any'],
    packages=[
        "emqx_extension", "emqx_extension"
    ],
    license='Apache License 2.0',
    install_requires=INSTALL_REQUIRES,
    python_requires='>=3.6.0',
    keywords=[
        'emqx',
        'emqx-extension'
    ]
)