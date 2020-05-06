import argparse
from .utils import good, bad
from .vsr import VERSION
import os




def main():
    # create argument parser object
    custom_usage = '\n' + \
        '  bass  \t\t: Git status\n'

    parser = argparse.ArgumentParser(
        description="CLI Utils - {} | 2020 Sameera Sandaruwan".format(VERSION), usage=custom_usage)

    parser.add_argument('-a', action='store_true', help="Git Add -A")


    parser.add_argument('comment', nargs='?', default=None)
    # parse the arguments from standard input
    args = parser.parse_args()

    print(args.__dict__)


if __name__ == "__main__":
    main()
