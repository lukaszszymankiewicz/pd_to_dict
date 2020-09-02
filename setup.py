import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pd_to_dict",
    version="0.0.1",
    author="Ukasz Szymankiewicz",
    author_email="lukasz_szymankiewicz@op.pl",
    description="Pretty dict from pandas",
    long_description=long_description,
    url="https://github.com/pypa/sampleproject",
    packages=["pandas>=0.23.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
