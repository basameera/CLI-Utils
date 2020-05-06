# clu

Python module for handling git easy.

## Features

* **<span style="color:red">Smart git fetch</span>**

**Only Python 3**

**Module can be accessed using both `eg` and `clu` commands**

``` bash
$ eg -h
usage: 
  clu                  : Git status
  clu comment          : Git add, commit (with "comment") and push
  clu -a               : Git Add -A
  clu -c comment       : Git Commit -m comment
  clu -p               : Git Push
  clu -u               : Git Pull
  clu -b <branch name> : Change branch

Easy Git | 2020 Sameera Sandaruwan

positional arguments:
  comment

optional arguments:
  -h, --help  show this help message and exit
  -a          Git Add -A
  -c          Git Commit -m comment
  -p          Git Push
  -u          Git Pull
  -b          Change branch
```

## Install

1. Clone this repo. ( `git clone https://github.com/basameera/clu.git` )
1. `cd clu` 
1. `pip install .` 

## Ideas

* pipreqs import handler method in skylynx
