from codecs import open
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as buff:
    long_description = buff.read()


setup(
    name="minimc",
    version="0.0.1.1",
    description="Just a little MCMC",
    long_description=long_description,
    author="Colin Carroll",
    author_email="colcarroll@gmail.com",
    url="https://github.com/ColCarroll/minimc",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=["test"]),
    install_requires=["autograd", "tqdm", "scipy"],
    include_package_data=True,
)
