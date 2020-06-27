# CLI-Utils

Python based command-line utility package.

**Only Python 3**

**Module can be accessed using both `clu` commands**

``` bash
$ clu -h
usage: clu [-h] [-t]

CLI Utils - 0.0.1 | 2020 Sameera Sandaruwan

optional arguments:
  -h, --help  show this help message and exit
  -t, --time  Print current time
```

## Install

1. Clone this repo. ( `git clone https://github.com/basameera/CLI-Utils.git` )
1. `cd clu` 
1. `pip3 install .` 
1. Add `export PATH=~/.local/bin:$PATH` to `~/.bashrc` file
1. `source ~/.bashrc`

## Ideas

* pipreqs import handler method in skylynx

## Problems

* import handler doesn't work properly. 
  * `pipreqs` produce wrong version for `torch`, `torchvision`.
  * Since my version use `pkg_resources`, the package has to be install for every venv. NOT GOOD.