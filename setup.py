# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe
from glob import glob

data_files = [("Microsoft.VC90.CRT", 
               ["Microsoft.VC90.CRT.manifest"] + glob(r'msvc*90.dll'))]

setup(
    name='twclient',
    version='1.0',
    description=u'A very simple Twitter client',
    author='yojyo@hotmail.com',
    author_email='yojyo@hotmail.com',
    url='http://www.geocities.jp/showa_yojyo/download/',
    windows=['twclient.pyw'],
    options={"py2exe":{"includes":["sip"]}},
    data_files=data_files)
