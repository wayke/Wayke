#!/usr/bin/env python
from setuptools import setup, find_packages
import pyrnassus
setup(
    name = "pyrnassus",
    version = "0.1",
    packages = ["pyrnassus"],
    author = "Javier Asensio-Cubero",
    author_email = "capitan.cambio@gmail.com",
    description = "muse-io 3.6.x compatible server",
    license = "MIT",
    keywords = "muse headband,muse-io,brain computer interfacing",
    install_requires=[
            "pyliblo>=0.9.1",
            "cython>=0.22",
            ],

)
