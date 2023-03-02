#!/usr/bin/env python

import setuptools

# Set your package requirements here
# use `mlcli build requirements` to autogenerate a `requirements.txt` file
requirements = [
    "click",
    "pumpkinpy==3.0.0",
    "pumpkinpy-client==3.0.0",
]

packages = setuptools.find_packages(exclude=["tests"])
packages += setuptools.find_namespace_packages(
    include=["instacart.*"]
)  # protos are a namespace package

setuptools.setup(
    name="qa-ranker",
    version='0.1.0',
    description="Algo to rank questions",
    author="@instacart/infra-ml",
    install_requires=requirements,
    packages=packages,
    entry_points={
            "console_scripts": [
                "qa_ranker_cli = qa_ranker.cli:main",
                "cli = qa_ranker.cli:main",
            ]
        }
)
