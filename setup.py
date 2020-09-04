import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='quickswitch',
    version='0.2.0',
    scripts=['qs'] ,
    author="Martin Hellstrom",
    author_email="martin@hellstrom.it",
    description="A utility to list directories within directories. Useful with fzf",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hellstromit/quickswitch",
    packages=setuptools.find_packages(),
    install_requires=[
        'pyfzf==0.2.2'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
