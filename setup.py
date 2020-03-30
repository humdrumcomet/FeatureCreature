import os
from setuptools import setup, find_packages

with open("README.md", "r") as fReadme:
    long_description = fReadme.read()

setup(
    name="FeatureCreature",
    version="0.0.0",
    author="Andrew Burry and Sacha Gunaratne and Aaron English",
    install_requires=[],
    packages=find_packages(),
)