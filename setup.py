from setuptools import setup

setup(
    name = 'myapp',
    version = '0.1.0',
    packages = ['cli-app'],
    entry_points = {'console_scripts': ['cli-app = cli-app.__main__:main']})
