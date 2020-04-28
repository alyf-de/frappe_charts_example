# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in frappe_charts/__init__.py
from frappe_charts import __version__ as version

setup(
	name='frappe_charts',
	version=version,
	description='xx',
	author='xx',
	author_email='xx',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
