#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     https://shop60459643.taobao.com
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2015/10/25
@desc:       
"""
import unittest
import os
import time
import sys
import HTMLTestRunner

# 将项目的目录加载到系统变量中
cur_dir = os.getcwd()
sys.path.append(cur_dir)

def gen_test_suite():
    testunit = unittest.TestSuite()
    # 定义测试文件查找的目录
    test_dir = os.path.abspath(os.path.dirname(__file__)) + '/test_case'
    # 注意：pattern，用来匹配/test_case目录下哪些用例加入本次运行
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_FAQ*.py',
                                                   top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit


if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(gen_test_suite())
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_folder = os.path.dirname(__file__) + os.path.sep + 'report' + os.path.sep
    filename = report_folder + now + '_result.html'  # 测试报告的路径名
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'XiaoICE项目自动化测试报告',
        description=u'用例执行情况：')
    all_test_units = gen_test_suite()
    runner.run(all_test_units)
    fp.close()  # 关闭生成的报告
