# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='FeatureExtractorPy',
    version='0.1.0',
    description='Feature extractor for assembly instructions',
    long_description=readme,
    author='Jed Walton',
    author_email='jedwalton98@@gmail.com',
    url='https://github.com/JedWalton/FeatureExtractorPy',
    license=license,
    packages=find_packages(exclude=('test', 'docs'))
)