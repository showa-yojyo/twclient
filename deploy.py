#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2012 プレハブ小屋 <yojyo@hotmail.com>
# All Rights Reserved.  NO WARRANTY.

"""A private script."""

import sys
import os
import shutil
import zipfile
from argparse import ArgumentParser

import twversion

__version__ = twversion.VERSION

DEST = r'D:\Dropbox\Public'

SDIST_OUTPUT = 'dist/twclient-0.0.0.zip'
PY2EXE_OUTPUT = 'twclient-0.0.0.win32'
PY2EXE_OUTPUT_ZIP = PY2EXE_OUTPUT + '.zip'

def main(args):
    # src
    shutil.copy2(SDIST_OUTPUT, DEST)

    # win32
    with zipfile.ZipFile(PY2EXE_OUTPUT_ZIP, 'w', zipfile.ZIP_DEFLATED) as fout:
        for root, dirs, files in os.walk(PY2EXE_OUTPUT):
            for file in files:
                p = os.path.join(root, file)
                fout.write(p, p)

    shutil.copy2(PY2EXE_OUTPUT_ZIP, DEST)
    os.remove(PY2EXE_OUTPUT_ZIP)

if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__, version=__version__)
    args = parser.parse_args()
    main(args)
