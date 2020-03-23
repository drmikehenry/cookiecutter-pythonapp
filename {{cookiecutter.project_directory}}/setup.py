#!/usr/bin/env python
# coding=utf-8

import setuptools

NAME = "{{cookiecutter.project_slug}}"
description = "TODO: Description."
keywords = "TODO: Keywords."


__version__ = None
for line in open("src/{}.py".format(NAME), encoding="utf-8"):
    if line.startswith("__version__"):
        __version__ = line.split('"')[1]
        break

with open("README.rst", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read()

with open("dev-requirements.txt", encoding="utf-8") as f:
    dev_requirements = f.read()

setuptools.setup(
    name=NAME,
    version=__version__,
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    py_modules=[NAME],
    python_requires=">=3.5",
    install_requires=requirements,
    extras_require={"dev": dev_requirements},
    entry_points={"console_scripts": ["{}={}:main".format(NAME, NAME)]},
    description=description,
    long_description=long_description,
    keywords=keywords,
    url="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}",
    author="{{cookiecutter.full_name}}",
    author_email="{{cookiecutter.email}}",
    license="MIT",
    zip_safe=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
