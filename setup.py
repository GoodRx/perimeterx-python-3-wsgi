#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='perimeterx-python-3-wsgi',
      license='MIT',
      description='PerimeterX Python 3 WSGI middleware',
      author='Johnny Tordgeman',
      author_email='johnny@perimeterx.com',
      url='https://github.com/PerimeterX/perimeterx-python-3-wsgi',
      packages=find_packages(exclude=['dev', 'test*']),
      package_data={'perimeterx': ['templates/*']},
      install_requires=['pystache>=0.5.4', 'requests>=2.22.0', 'Werkzeug==0.16.0', 'pycryptodome>=3.9.0'],
      classifiers=['Intended Audience :: Developers',
                   'Programming Language :: Python :: 3.7'])
