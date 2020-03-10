import os
import setuptools

with open('README.md', 'r') as fReadme:
    long_description = fReadme = fReadme.read()

setuptools.setup(
    name='FeatureCreature',
    version='0.0.0',
    author='Andrew Burry and Sacha Gunaratne and Aaron English',
    install_requires=[],
    packages=setuptools.find_packages(),
)
