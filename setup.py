# -*- coding: utf-8 -*-

# Some codes borrowed from:
# http://all.marlix.com/openerp/client/openerp-client-6.0.3/setup.py

import sys
import os
from distutils.core import setup
import py2exe
from glob import glob

def data_files():
    files = []
    files.append((".", ["README.txt", "timelines.ini.sample",]))
    if sys.platform == 'win32':
        files.append(("Microsoft.VC90.CRT", 
                      ["Microsoft.VC90.CRT.manifest"] + glob(r'msvc*90.dll')))
    return files

options = {
    "py2exe":{
        "dist_dir": 'dist',
        "includes":["sip"]
        }
    }

setup(
    name='twclient',
    version='',
    description=u'A very simple Twitter client',
    author='yojyo@hotmail.com',
    author_email='yojyo@hotmail.com',
    url='http://www.geocities.jp/showa_yojyo/download/twclient.html',
    windows=['twclient.pyw'],
    options=options,
    data_files=data_files())

if sys.argv[-1] == 'py2exe':
    import dateutil
    import zipfile

    # Make sure the layout of dateutil hasn't changed
    assert (dateutil.__file__.endswith('__init__.pyc') or
            dateutil.__file__.endswith('__init__.py')), dateutil.__file__
    zoneinfo_dir = os.path.join(os.path.dirname(dateutil.__file__), 'zoneinfo')
    # '..\\Lib\\dateutil\\__init__.py' -> '..\\Lib'
    disk_basedir = os.path.dirname(os.path.dirname(dateutil.__file__))
    zipfile_path = os.path.join(options['py2exe']['dist_dir'], 'library.zip')
    print zipfile_path
    z = zipfile.ZipFile(zipfile_path, 'a')

    for absdir, directories, filenames in os.walk(zoneinfo_dir):
        assert absdir.startswith(disk_basedir), (absdir, disk_basedir)
        zip_dir = absdir[len(disk_basedir):]
        for f in filenames:
            z.write(os.path.join(absdir, f), os.path.join(zip_dir, f))

    z.close()
