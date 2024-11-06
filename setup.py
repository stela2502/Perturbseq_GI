from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="perturbseq",
    version="0.1.0",
    packages=["perturbseq", "onesense", "maxide"],
    install_requires=required,
)

