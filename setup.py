# -*- coding: utf-8 -*-

# Some codes borrowed from:
# http://all.marlix.com/openerp/client/openerp-client-6.0.3/setup.py

import sys
import os
from distutils.core import setup
import py2exe
from glob import glob
import twversion

def make_data_files(use_py2exe):
    files = []
    files.append((".", ["README.txt", "timelines.ini.sample",]))
    if use_py2exe:
        files.append(("Microsoft.VC90.CRT", 
                      ["Microsoft.VC90.CRT.manifest"] + glob(r'msvc*90.dll')))
    return files

def make_options(use_py2exe):
    if use_py2exe:
        return {
            "py2exe":{
                "dist_dir": 'twclient-{0}.win32'.format(twversion.VERSION),
                "includes":["sip"]
                }
            }
    else:
        return {}

def main():
    use_py2exe = sys.platform == 'win32' and 'py2exe' in sys.argv

    options = make_options(use_py2exe)
    
    setup(
        name='twclient',
        version='',
        description=u'A very simple Twitter client',
        author='yojyo@hotmail.com',
        author_email='yojyo@hotmail.com',
        url='http://www.geocities.jp/showa_yojyo/download/twclient.html',
        windows=['twclient.pyw'],
        options=options,
        data_files=make_data_files(use_py2exe))

    if use_py2exe:
        import dateutil
        import zipfile

        # Make sure the layout of dateutil hasn't changed
        assert (dateutil.__file__.endswith('__init__.pyc') or
                dateutil.__file__.endswith('__init__.py')), dateutil.__file__

        # D:\Python26\lib\site-packages\dateutil\zoneinfo
        zoneinfo_dir = os.path.join(os.path.dirname(dateutil.__file__), 'zoneinfo')

        # D:\Python26\lib\site-packages
        disk_basedir = os.path.dirname(os.path.dirname(dateutil.__file__))
        zipfile_path = os.path.join(options['py2exe']['dist_dir'], 'library.zip')
        z = zipfile.ZipFile(zipfile_path, 'a')

        for absdir, directories, filenames in os.walk(zoneinfo_dir):
            assert absdir.startswith(disk_basedir), (absdir, disk_basedir)
            zip_dir = absdir[len(disk_basedir):]
            for f in filenames:
                if f.endswith('.tar.gz'):
                    z.write(os.path.join(absdir, f), os.path.join(zip_dir, f))

        z.close()

if __name__ == '__main__':
    main()
