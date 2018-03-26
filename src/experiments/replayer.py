#!/usr/bin/env python

"""This is the example module.

This module does stuff.
"""

import os, sys, logging, json


__author__ = "Wai Lam Jonathan Lee"
__email__ = "walee@uc.cl"
__all__ = [ 'MonolithicReplayer', 'RecompositionReplayer' ]


to_add = os.path.abspath(__file__)
to_add = to_add.split(os.sep)[:-2]
sys.path.append(os.sep.join(to_add))


logger = logging.getLogger(__name__)


class MonolithicReplayer:
    def __init__(self, configs, outdir, prom_executor):
        self.outdir = outdir
        self.configs = configs
        self.prom_executor = prom_executor

    def replay(self):
        self.prom_executor.execute()

class RecompositionReplayer:
    def __init__(self, configs, outdir, prom_executor):
        self.outdir = outdir
        self.configs = configs
        self.prom_executor = prom_executor

    def replay(self):
        self.prom_executor.execute()

