import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

def get_version():
    version_file = "app/_version.py"
    with open(version_file) as f:
        exec(compile(f.read(), version_file, "exec"))
    return(locals()["__version__"])

quickswitch_version = get_version()

setuptools.setup(
    name='quickswitch',
    version=quickswitch_version,
    scripts=['qs'] ,
    author="Martin Hellstrom",
    author_email="martin@hellstrom.it",
    description="A utility to find subdirectories using fzf",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hellstromit/quickswitch",
    packages=setuptools.find_packages(),
    install_requires=[
        'iterfzf==0.5.0.20.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
