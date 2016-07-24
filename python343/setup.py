#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
# setup.py
 
from distutils.core import setup
import py2exe
setup(
    data_files = [('',['program.bmp','program.jpg'])],
    windows = [
    {
        "script": "deleteBkFiles.py",
        "icon_resources": [(1, "app.ico")]
    }
    ],
)