import argparse
from .utils import good, bad
from .vsr import VERSION
import os
import pkg_resources
import numpy as np
import pandas as pd
import seaborn as sns
import skylynx
import tqdm
import numba

def read_req(fname):

    output_str = ''
    if os.path.isfile(fname):
        with open(fname) as f:
            content = f.readlines()
            for line in content:
                module = line.rstrip().split('==')[0]
                local_version = pkg_resources.get_distribution(module).version
                output_str += '{}=={}\n'.format(module, local_version)
    else:
        raise AttributeError('No \'{}\' file.'.format(fname))

    with open(fname, 'w') as outfile:
        outfile.write(output_str)


def main():
    # create argument parser object
    # custom_usage = '\n' + \
    #     '  clu  \t\t: []\n'

    # U+1F600

    description = "CLI Utils - {} | 2020 Sameera Sandaruwan".format(VERSION)

    parser = argparse.ArgumentParser(
        description=description, usage=None)

    # optional args
    parser.add_argument('-t', '--time', action='store_true',
                        help="Print current time")
    parser.add_argument('--pipreqs', action='store_true',
                        help="Generate requirements.txt")

    # positional args
    # parser.add_argument('comment', nargs='?', default=None)

    args = parser.parse_args()

    # print(args.__dict__)

    if args.time:
        import time
        print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(time.time())))

    elif args.pipreqs:
        # TODO: use `conda env export > environment_droplet.yml` as well

        req_file = 'requirements.txt'

        path_folder = os.getcwd()

        # use pipreqs to generate requirements.txt
        os.system('pipreqs --force --savepath {} {}'.format(req_file, path_folder))

        read_req(req_file)

    else:
        print(u'\U0001f604', description, u'\U0001f604')


if __name__ == "__main__":
    main()
