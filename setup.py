#!/usr/bin/python
# coding: utf8

from codecs import open
import re

try:
    import setuptools
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('src/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

requires = ['requests', 'setuptools', 'requests_mock', 'swagger', 'connexion']

setup(
    name='simpleNetworkService',
    version=version,
    description="SimpleNetworkService is a simple and consistent geocoding service which resolves Lat and Long to a address.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Yuvaraj',
    author_email='yuv.swt@gmail.com',
    url='https://github.com/uvraj88/SimpleNetworkService',
    download_url='https://github.com/uvraj88/SimpleNetworkService',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    keywords='google here addressResolver',
)
