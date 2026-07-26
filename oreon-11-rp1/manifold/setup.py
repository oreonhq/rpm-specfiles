# SPDX: unlicense
# Modified from https://github.com/maximiliank/cmake_python_r_example/blob/master/src/Python/setup.py.in

from setuptools import setup
from setuptools.dist import Distribution
import sys


class BinaryDistribution(Distribution):
    """Distribution which always forces a binary package with platform name"""
    def has_ext_modules(foo):
        return True

setup(
    include_package_data=True,
    py_modules=['manifold3d'],
    packages=find_packages(
        where='.',
        exclude=['build','CMakeFiles'],
    ),
    package_data={
        '': ['manifold3d*.so', 'manifold3d.pyi']
    },
    distclass=BinaryDistribution
)
