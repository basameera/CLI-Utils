import argparse
from .utils import good, bad
from .vsr import VERSION
import os


def main():
    # create argument parser object
    custom_usage = '\n' + \
        '  clu  \t\t: []\n'

    description = "CLI Utils - {} | 2020 Sameera Sandaruwan".format(VERSION)

    parser = argparse.ArgumentParser(
        description=description, usage=None)

    parser.add_argument('-t', '--time', action='store_true', help="Print current time")

    # parser.add_argument('comment', nargs='?', default=None)
    # parse the arguments from standard input
    args = parser.parse_args()

    # print(args.__dict__)

    if args.time:
        import time
        print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(time.time())))

    else:
        print(description)


if __name__ == "__main__":
    main()
