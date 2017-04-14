#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@others:     DTStudio, All rights reserved-- Created on 2017/03/29
@desc:       使用unittest组织用例
"""
from selenium import webdriver
import unittest
import time


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://csint.msxiaobing.com/"
        self.driver.get(self.base_url)
        #   int环境，15810189481的手机号cookie
        add_cookie = [{'value': 'true', 'name': 'isQqQrCodeShown'}, {'value': 'E913C694C82D08FAA7C8C3F632644D2C', 'name': 'salt'}, {'value': 'd6615295f92e35a4fc39e36bff91c1f8f015b9a1729023858a4ef3c8bad31c98', 'name': 'ARRAffinity'}, {'value': '3y2bsmcm11cx5uh1tidz1q3j', 'name': 'ASP.NET_SessionId'}, {'value': 'YDVasiE2QkhaNFFJeUkuTMtMEEpnMd4wWrFEN1pPL0xNAA', 'name': 'cpid'}, {'value': 'xdge3nE9mGhqhYm0nb8doTqSoufM6RUiuU-b7v4Oz4aCxC79nBkGlOAalBwc5ILjj0t0HaANd3wrsdyXUUEPsq0MXZ9WcaAx7mM-3lRYKLU1', 'name': '__RequestVerificationToken'}, {'value': '1', 'name': '_gat'}, {'value': 'GA1.2.2047437516.1489842596', 'name': '_ga'}, {'value': '9FB5B8CA00779E60FC40814D6359DF4EB5DB6E35CFD91A122F6F208E2594C2E8AFCE37B0AD392232F47AEAE6E3F68D27F626B3BEDBCD77312FDD456C528600C62A6E28AF013571E8EFA69740B7178CB3', 'name': '.ASPXAUTH'}, {'value': 'EulaAcceptance201703', 'name': 'ForceSignOut'}, {'value': 'true', 'name': 'isQqQrCodeShown'}]
        #   prod环境，13718161821的手机号cookie
        # add_cookie = [{'value': 'fcfe77ea6824afb8624e05c93de1dd5932aaa6cbb5c35316ae3c0aa618edf44d', 'name': 'ARRAffinity'}, {'value': 'YE0lNllLRDJeTlRNeDFUMzO0lDBgSSVJJk1BN11LVrJPAA', 'name': 'cpid'}, {'value': 'opmgxjw0lpyawp2t4yldwoxq', 'name': 'ASP.NET_SessionId'}, {'value': 'uPELacUPOQ43D8t9Ymta2zpdtGzGHGMqxXBYTImp0CK1ewd-C-Ae9BkT3HDexhCkXtZs-pkeRzOwMIAy0RsQ1j19gLcSIOvy-G8SetkBLMg1', 'name': '__RequestVerificationToken'}, {'value': 'GA1.2.2117121162.1490166469', 'name': '_ga'}, {'value': '1', 'name': '_gat'}, {'value': '67B514E7BDD4F4309890731099D101877D657BF1874E8D3F0542D6939CCBC9A7C2F8FF09E519366DEF3994039BF692396058FB6637CAA95D02F7B02F9C435DDD0FCC7DE2538E8122676A9482DE3AFD4A', 'name': '.ASPXAUTH'}, {'value': 'EulaAcceptance201703', 'name': 'ForceSignOut'}, {'value': '736C7959BCC6EA7736BA7B6E6511A0F6', 'name': 'salt'}, {'value': 'true', 'name': 'isQqQrCodeShown'}]
        for i in range(0, len(add_cookie)):
            self.driver.add_cookie(add_cookie[i])

    def test_FAQ_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("平台测试账号").click()
        driver.find_element_by_link_text('知识库').click()
        # login = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[2]/div/div[2]/div/section/div[2]/ul/li[2]/button').click()
        # # login.find_element_by_id('addPrimary').send_keys('你好！')
        # return login

    # def test_FAQ_add(self, login):
    #     login.find_element_by_id('addPrimary').send_keys('你好！')

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
