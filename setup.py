from setuptools import setup
from bass import __version__, __author__, __author_email__

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="bass",
    version=__version__,
    description="Python Easy Git",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/basameera/bass",
    author=__author__,
    author_email=__author_email__,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["bass"],
    include_package_data=True,
    # install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "bass=bass.cli:main",
            "rk=bass.cli:main",
        ]
    },
)