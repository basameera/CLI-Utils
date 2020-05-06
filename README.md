# bass

Python module for handling git easy.

## Features

* **<span style="color:red">Smart git fetch</span>**

**Only Python 3**

**Module can be accessed using both `eg` and `bass` commands**

``` bash
$ eg -h
usage: 
  bass                  : Git status
  bass comment          : Git add, commit (with "comment") and push
  bass -a               : Git Add -A
  bass -c comment       : Git Commit -m comment
  bass -p               : Git Push
  bass -u               : Git Pull
  bass -b <branch name> : Change branch

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

1. Clone this repo. ( `git clone https://github.com/basameera/bass.git` )
1. `cd bass` 
1. `pip install .` 

**Git fetch**

``` 
UPSTREAM=${1:-'@{u}'}
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse "$UPSTREAM")
BASE=$(git merge-base @ "$UPSTREAM")

echo LOCAL : $LOCAL
echo REMOTE: $REMOTE
echo BASE : $BASE

if [ $LOCAL = $REMOTE ]; then
    echo "Up-to-date"
elif [ $LOCAL = $BASE ]; then
    echo "Need to pull"
elif [ $REMOTE = $BASE ]; then
    echo "Need to push"
else
    echo "Diverged"
fi
```

## Ideas

* pipreqs import handler method in skylynx
