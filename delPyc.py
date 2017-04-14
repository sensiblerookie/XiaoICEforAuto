#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     https://shop60459643.taobao.com
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2015/10/29
@desc:       删除pyc编译文件
"""
import os


def del_pyc():
    for folder, folders, files in os.walk('.'):
        for filename in files:
            root, ext = os.path.splitext(filename)
            if ext == '.pyc':
                print(os.path.abspath(os.path.join(folder, filename)), os.remove(os.path.abspath(os.path.join(folder, filename))))

if __name__ == "__main__":
    del_pyc()