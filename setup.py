from setuptools import setup
from clu import __version__, __author__, __author_email__

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="clu",
    version=__version__,
    description="Python based CLI Utils | 2020 Sameera Sandaruwan",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/basameera/clu",
    author=__author__,
    author_email=__author_email__,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["clu"],
    include_package_data=True,
    # install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "clu=clu.cli:main",
            "rk=clu.cli:main",
        ]
    },
)