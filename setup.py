from setuptools import setup
from setuptools import find_packages, setup

import json


with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='noaawc',
    version='0.0.12',
    url='https://github.com/perseu912/noaawc',
    license='GPLv3',
    author='Reinan Br',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='slimchatuba@gmail.com',
    keywords='climate weather noaa plots',
    description=u'Library for plotting dataset from noaa site in basemap',
    packages=find_packages(),
    install_requires=['numpy','noawclg','matplotlib','pandas','psutil','imageio','basemap'],)
