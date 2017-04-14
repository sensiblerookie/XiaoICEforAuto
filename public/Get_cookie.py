# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)
base_url = "http://csint.msxiaobing.com/"
driver.get(base_url)

driver.find_element_by_id('phoneNumber').send_keys('15810189481')
driver.find_element_by_id('sendverification').click()
ip = input('请输入验证码：')
driver.find_element_by_id('verification').send_keys(ip)
driver.find_element_by_class_name('sbtn').click()

cookie = driver.get_cookies()

print('{\'name\': \'%s\', \'value\':\' %s\'}' % (cookie['name'], cookie['value']))


