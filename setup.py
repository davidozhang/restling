# -*- coding: utf-8 -*-

from setuptools import setup


with open('requirements.txt') as fp:
    dependencies = [l.strip() for l in fp.readlines()]

setup(
    name='Restling',
    version='1.0',
    author='David Zhang',
    author_email='davzee@hotmail.com',
    url='http://github.com/davidozhang/restling',
    description='Restling API Service',
    packages=['restling'],
    install_requires=dependencies,
    test_suite='nose.collector',
)
