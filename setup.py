# coding=utf-8
from setuptools import setup

setup(
    name="parenthetics",
    description="Codefellows 401 Parenthetics Assignment",
    version=0.1,
    author="Mike Harrison",
    author_email="",
    license="MIT",
    py_modules=["parenthetics"],
    package_dir={"": "src"},
    install_requires=['future'],
    extras_require={
        'test': ['pytest', 'tox']
    },
)
