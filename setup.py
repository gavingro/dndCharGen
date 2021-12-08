from setuptools import setup, find_packages

setup(
    name='',
    version='0.1',
    packages=find_packages(exclude=['test*']),
    license='MIT',
    description='A python package to generate a D&D character and populate a character sheet.',
    install_requires=["pdfrw = 0.4"],
    url='https://github.com/gavingro/DATA533proj3_dndCharGen.git',
    author='Gavin, Kevin',
    author_email='eeeeemail@mail.rus'
)