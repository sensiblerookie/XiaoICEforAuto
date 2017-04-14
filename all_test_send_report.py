#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     https://shop60459643.taobao.com
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2015/9/25
@desc:       
"""
import unittest
import os
import sys
import time
import smtplib
from email.mime.text import MIMEText
from public import HTMLTestRunner

# 将项目的目录加载到系统变量中
cur_dir = os.getcwd()
sys.path.append(cur_dir)


def send_mail(file_new):
    # 发件人邮箱
    mail_from = 'v-fuyli@microsoft.com'
    # 收件人邮箱
    mail_to = 'v-fuyli@microsoft.com'
    # 定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    # 定义标题
    msg['Subject'] = u"ICE自动化测试报告"
    # 定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp = smtplib.SMTP()
    # 连接 SMTP 服务器，此处用的 126 的 SMTP 服务器
    smtp.connect('smtp.outlook.com')
    # 发件人的用户名密码
    smtp.login('v-fuyli@microsoft.com', 'yuan?009')
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print('email has send out !')


# ======查找测试报告目录，找到最新生成的测试报告文件====
def send_report(report_folder):
    result_dir = report_folder
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
    # print (u'最新测试生成的报告： '+lists[-1])
    # 找到最新生成的文件
    file_new = os.path.join(result_dir, lists[-1])
    print(file_new)
    # 调用发邮件模块
    send_mail(file_new)


def gen_test_suite():
    testunit = unittest.TestSuite()
    # 定义测试文件查找的目录
    test_dir = os.path.abspath(os.path.dirname(__file__)) + '/test_case'
    # 注意：pattern，用来匹配/test_case目录下哪些用例加入本次运行
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_01*.py',
                                                   top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_folder = os.path.dirname(__file__) + os.path.sep + 'report' + os.path.sep
    filename = report_folder + now + 'result.html'
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'ICE项目自动化测试报告',
        description=u'用例执行情况：')
    all_test_units = gen_test_suite()
    runner.run(all_test_units)
    fp.close()  # 关闭生成的报告
    send_report(report_folder)  # 发送报告

    # 此文件和 all_test.py的区别在于，多了一步：send_report(test_report)
