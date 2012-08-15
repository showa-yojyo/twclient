# -*- coding: utf-8 -*-
u"""
Copyright (c) 2012 プレハブ小屋管理人 <yojyo@hotmail.com>
All Rights Reserved.  NO WARRANTY.

A private script.
"""

import sys
import os
import shutil
import zipfile

DEST = r'D:\Dropbox\Public'

SDIST_OUTPUT = 'dist/twclient-0.0.0.zip'
PY2EXE_OUTPUT = 'twclient-0.0.0.win32'
PY2EXE_OUTPUT_ZIP = PY2EXE_OUTPUT + '.zip'

def main():
    # src
    shutil.copy2(SDIST_OUTPUT, DEST)

    # win32
    fout = zipfile.ZipFile(PY2EXE_OUTPUT_ZIP, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(PY2EXE_OUTPUT):
        for file in files:
            p = os.path.join(root, file)
            fout.write(p, p)
    fout.close()

    shutil.copy2(PY2EXE_OUTPUT_ZIP, DEST)
    os.remove(PY2EXE_OUTPUT_ZIP)

if __name__ == '__main__':
    main()
