#!/usr/bin/env python

"""This is the example module.

This module does stuff.
"""


import csv
from datetime import datetime as dt
import logging, os, json, sys
import logging.config

__author__ = "Wai Lam Jonathan Lee"
__email__ = "walee@uc.cl"

to_add = os.path.abspath(__file__)
to_add = to_add.split(os.sep)[:-3]
sys.path.append(os.sep.join(to_add))


def writeheader(fpath, header):
    f = open(fpath, 'w')
    writer = csv.writer(f)
    writer.writerow(header)
    f.close()


def gen_dirname_from_dt():
    return dt.now().strftime('%d-%m-%Y_%H-%M-%S-%f')


def __get_keypath(key, _dict, level=None, paths=None):
    if level is None:
        level = []
    if paths is None:
        paths = []
    # each path is a list
    if key in _dict:
        path = level + [key]
        paths.append(path)

    # recursively search in children which are dict
    for key0, val in _dict.items():
        if isinstance(val, dict):
            level0 = level + [key0]
            paths = paths + __get_keypath(key, val, level=level0)

    return paths


def append_to_dir(val, path, _dict):
    if len(path) == 1:
        # just update
        key = path[0]
        _dict[key] = val + _dict[key]
    else:
        # go one level deeper
        _dict = _dict[path.pop(0)]
        append_to_dir(val, path, _dict)


def setup_logging(logdir='.',
                  default_path='logging.json',
                  default_level=logging.INFO,
                  env_key='LOG_CFG'):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    print('Logger configuration filepath: {}'.format(path))
    if os.path.exists(path):
        print('loading logger configurations...')
        with open(path, 'rt') as f:
            config = json.load(f)

        # configure the output directory of handlers
        paths = __get_keypath('filename', config)
        for path in paths:
            # update with logdir
            to_update = logdir + os.sep
            append_to_dir(to_update, path, config)

        logging.config.dictConfig(config)
    else:
        # load the basic configuration
        logging.basicConfig(level=default_level)
