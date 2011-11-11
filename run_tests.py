#!/usr/bin/env python
#TODO: see http://readthedocs.org/docs/nose/en/latest/plugins/testing.html
import nose
import os.path
import sys
from graph_runner import GraphRunner

if __name__ == '__main__':
    new_args = list(sys.argv)
    new_args.append('--with-graphrunner')
    new_args.append('./testapp')
    nose.main(addplugins=[GraphRunner()], argv=new_args)
