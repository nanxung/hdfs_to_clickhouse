#!/usr/bin/env python
# coding=utf-8
from setuptools import setup, find_packages
setup(
    name='hdfs_to_clickhouse',
    version=0.1,
    description=(
        '通过pyspark读取hdfs上文件，导入clickhouse中'
    ),
    author='chen',
    author_email='chenpu290@gmail.com',
    maintainer='chen',
    maintainer_email='chenpu290@gmail.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/nanxung/hdfs_to_clickhouse.git',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)