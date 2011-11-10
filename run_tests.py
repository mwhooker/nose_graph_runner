#!/usr/bin/env python

import nose
import sys
from graph_runner import GraphRunner

if __name__ == '__main__':
    new_args = list(sys.argv)
    new_args.append('--with-graphrunner')
    nose.main(addplugins=[GraphRunner()], argv=new_args)
