from setuptools import setup
from setuptools import find_packages

setup(
    name='compoyse',
    version='0.0.1',
    packages = find_packages(include = ['compoyse', 'compoyse.*']),
    install_requires=[
        'pyaudio',
        'pretty_midi'
    ]
)