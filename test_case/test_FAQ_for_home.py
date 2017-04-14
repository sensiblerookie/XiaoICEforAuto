# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest
import time


class TestSearch(unittest.TestCase):
    '''FAQ首页测试'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://csint.msxiaobing.com/"
        self.driver.get(self.base_url)


        # add_cookie = [{'value': 'true', 'name': 'isQqQrCodeShown'}, {'value': 'E913C694C82D08FAA7C8C3F632644D2C', 'name': 'salt'}, {'value': 'd6615295f92e35a4fc39e36bff91c1f8f015b9a1729023858a4ef3c8bad31c98', 'name': 'ARRAffinity'}, {'value': '3y2bsmcm11cx5uh1tidz1q3j', 'name': 'ASP.NET_SessionId'}, {'value': 'YDVasiE2QkhaNFFJeUkuTMtMEEpnMd4wWrFEN1pPL0xNAA', 'name': 'cpid'}, {'value': 'xdge3nE9mGhqhYm0nb8doTqSoufM6RUiuU-b7v4Oz4aCxC79nBkGlOAalBwc5ILjj0t0HaANd3wrsdyXUUEPsq0MXZ9WcaAx7mM-3lRYKLU1', 'name': '__RequestVerificationToken'}, {'value': '1', 'name': '_gat'}, {'value': 'GA1.2.2047437516.1489842596', 'name': '_ga'}, {'value': '9FB5B8CA00779E60FC40814D6359DF4EB5DB6E35CFD91A122F6F208E2594C2E8AFCE37B0AD392232F47AEAE6E3F68D27F626B3BEDBCD77312FDD456C528600C62A6E28AF013571E8EFA69740B7178CB3', 'name': '.ASPXAUTH'}, {'value': 'EulaAcceptance201703', 'name': 'ForceSignOut'}, {'value': 'true', 'name': 'isQqQrCodeShown'}]
        # for i in range(0, len(add_cookie)):
            self.driver.add_cookie(add_cookie[i])

    def test_FAQ_home(self):
        '''检查是否可以进入首页'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_class_name('guide_button').click()
        driver.find_element_by_link_text("平台测试账号").click()
        driver.find_element_by_link_text('知识库').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="faq_guide"]/div/div[3]/button').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="faq_guide"]/div/div[3]/button').click()
        time.sleep(10)


    # def test_FAQ_time(self):
    #     '''检查更新时间是否可以用'''
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     driver.find_element_by_link_text("平台测试账号").click()
    #     driver.find_element_by_link_text('知识库').click()






    def tearDown(self):
        time.sleep(5)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
