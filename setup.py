from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path


setup(
    name='papysql',
    packages=find_packages(),
    version='0.2.3',
    long_description='This is a library to interface SQL with python. The basic library read the tables with list_tables method and read them with display_table. When a table is red is then converted into a pandas DataFrame. Moreover it gives the possibility to read a SQL script that builds a db with ExecuteScriptFromFile',
    author='Francesco Gualdi',
    license='GPL'
)
