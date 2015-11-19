#!/usr/bin/env python
# -*- coding:utf-8 -*-

from distutils.core import setup

from inline import __version__ as version


setup(
    name='inline',
    version=version,
    description='embed inline C / C++ source codes in Python',
    long_description=open('README.rst').read(),
    author='Ryosuke Ito',
    author_email='rito.0305@gmail.com',
    url='https://github.com/manicmaniac/inline',
    keywords='c c++ inline compile',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: C',
        'Programming Language :: C++',
        'Topic :: Software Development',
    ],
    py_modules=['inline'],
)
