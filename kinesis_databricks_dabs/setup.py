"""
setup.py configuration script describing how to build and package this project.

This file is primarily used by the setuptools library and typically should not
be executed directly. See README.md for how to deploy, test, and run
the kinesis_databricks_dabs project.
"""
from setuptools import setup, find_packages

import sys
sys.path.append('./src')

import kinesis_databricks_dabs

setup(
    name="kinesis_databricks_dabs",
    version=kinesis_databricks_dabs.__version__,
    url="https://databricks.com",
    author="yashbaviskar@propensitylabs.com",
    description="wheel file based on kinesis_databricks_dabs/src",
    packages=find_packages(where='./src'),
    package_dir={'': 'src'},
    entry_points={
        "packages": [
            "main=kinesis_databricks_dabs.main:main"
        ]
    },
    install_requires=[
        # Dependencies in case the output wheel file is used as a library dependency.
        # For defining dependencies, when this package is used in Databricks, see:
        # https://docs.databricks.com/dev-tools/bundles/library-dependencies.html
        "setuptools"
    ],
)
