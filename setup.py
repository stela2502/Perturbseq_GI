from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="my_package",
    version="0.1.0",
    packages=["my_package"],
    install_requires=required,
)

