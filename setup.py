from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sunmetals/__init__.py
from sunmetals import __version__ as version

setup(
	name="sunmetals",
	version=version,
	description="Manufacturer of Aluminium Products",
	author="Thirvusoft",
	author_email="sunbrandindia@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
