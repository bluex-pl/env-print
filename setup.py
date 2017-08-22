#!/usr/bin/env python3

from setuptools import setup

setup(
    name='env_print',
    version='1.0',
    packages=['env_print'],
    entry_points = {
        'console_scripts': ['env-print=env_print.env_print:main'],
    }
)

