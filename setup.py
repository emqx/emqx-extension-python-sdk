#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup


INSTALL_REQUIRES = []

setup(
    name='emqx_sdk',
    version='0.1',
    author='emqx',
    author_email='sdk@emqx.io',
    url='https://github.com/emqx/emqx_sdk',
    description='emqx sdk',
    long_description=open("README.rst").read(),
    platforms=['any'],
    license='MIT',
    install_requires=INSTALL_REQUIRES,
    python_requires='>=3.6.0',
    keywords=[
        'emqx',
    ]
)