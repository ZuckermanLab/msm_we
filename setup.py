#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

setup(
    name="msm_we",
    version="1.0.1",
    author="John Russo, Sagar Kania, Jeremy Copperman, Daniel Zuckerman",
    author_email="zuckermd@ohsu.edu",
    description="Code for Markov state modeling of weighted ensemble trajectories.",
    url="https://github.com/ZuckermanLab/msm_we",
    packages=find_packages(include=["msm_we", "msm_we.*"]),
    entry_points={
        "console_scripts": [
            "msm_we=msm_we.cli:main"
        ]
    },
    license="MIT license",
    include_package_data=True,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.5",
    zip_safe=False,
)

