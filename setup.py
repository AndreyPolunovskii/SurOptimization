from setuptools import setup, find_packages
from os.path import join, dirname, isfile


FILE_REQS = 'requirements.txt'
if isfile(FILE_REQS):
    with open(FILE_REQS, 'r') as f:
        reqs = f.read().splitlines()

setup(
    name='surmin',
    version='1.0.5',
    packages=find_packages(),
    install_requires=reqs,
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    include_package_data=True,
)
