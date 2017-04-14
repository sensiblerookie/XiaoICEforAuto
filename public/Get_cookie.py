# -*- coding: utf-8 -*-
from selenium import webdriver

# driver = webdriver.Chrome()
# driver.implicitly_wait(30)
# base_url = "http://csint.msxiaobing.com/"
# driver.get(base_url)
# #
# driver.find_element_by_id('phoneNumber').send_keys('15810189481')
# driver.find_element_by_id('sendverification').click()
# ip = input('请输入验证码：')
# driver.find_element_by_id('verification').send_keys(ip)
# driver.find_element_by_class_name('sbtn').click()
# driver.find_element_by_class_name('guide_button').click()
#
# txt = open('cookie.txt', 'w+')
# txt.write('[')
# for cookie in driver.get_cookies():
#     txt.writelines('{\'value\': \'%s\', \'name\': \' %s\'}, ' % (cookie['value'], cookie['name']))
# txt.write('{\'value\': \'true\', \'name\': \'isQqQrCodeShown\'}]')
# txt.close()
#
# f = open('cookie.txt', 'r')
# # add_cookie = [{'value': '9ADE3954F3B4EA14E3C2ECF95CAA44A0', 'name': ' salt'}, {'value': '330668c806b75cdab4f68059491ca3d63e6e89ca6482b1be0fea83130f3d4e5b', 'name': ' ARRAffinity'}, {'value': 'dpz33x0qcqnymc1a35sgszo0', 'name': ' ASP.NET_SessionId'}, {'value': 'GDXesCFMxLRcNVNJfklUNTOyFEpiMF83WTRFMiU0LzRPAA', 'name': ' cpid'}, {'value': 'PvVAkRLnvfiAG2YpL0ZPplnqFKF3BaLP4cmTKQDv7MwzrfC1TbXCbbNwOWZj_Y68JuOjTWSTenz86WwkTzlj4ZKEWMv3ErutS0goXP5WkNU1', 'name': ' __RequestVerificationToken'}, {'value': '1', 'name': ' _gat'}, {'value': 'GA1.2.753731095.1492159007', 'name': ' _ga'}, {'value': '725A884969598F6BCD79C54A79913FB10E4423C1C1736B7722BB51209D643074C923155BA4E166A4EAA14FF363C644C393BFF86F1495681B26115E59242A8699DA7A1A0BAC1674C415B77B890CAAFCE6', 'name': ' .ASPXAUTH'}, {'value': 'EulaAcceptance201703', 'name': ' ForceSignOut'}, {'value': 'true', 'name': ' isQqQrCodeShown'}, {'value': '30', 'name': ' hideFaqGuideInHome'}, {'value': 'true', 'name': 'isQqQrCodeShown'}]
# add_cookie = [{'value': '30', 'name': 'hideFaqGuideInHome'},
#               {'value': 'D32D51A9DE047D4622A38E4F292B5B84', 'name': 'salt'},
#               {'value': '330668c806b75cdab4f68059491ca3d63e6e89ca6482b1be0fea83130f3d4e5b', 'name': 'ARRAffinity'},
#               {'value': 'ruu1zpdmenm5leujodag1umc', 'name': 'ASP.NET_SessionId'},
#               {'value': 'GEsnTlhMQUoiTtE0eklXTcw0F0tgSSVJJzRCsFg2KUtOAA', 'name': 'cpid'},
#               {'value': 'i-HBnctXeq9GX2NR9zbw4UgWs-BYY2ZQf0qSTDYXIrmrrDY8iOCwqBB5lXRPulXvDHHw3T-TBY7E310FIAERFl3WFHdMTdebt9QGyvnwZLk1', 'name': '__RequestVerificationToken'},
#               {'value': 'GA1.2.32620240.1492159845', 'name': '_ga'},
#               {'value': 'E1C59EB04299B25B5E673298B5E2F2CB5CF297C6F64984F7DF2D15057CDAADAA23A778D1814BAE6B6E555AC4C48F13305CC2F6195F08D9E350EBA2A3BD98F084547B8A670B099B18C6189E6DDEB7DCF5', 'name': '.ASPXAUTH'},
#               {'value': 'EulaAcceptance201703', 'name': 'ForceSignOut'},
#               {'value': 'true', 'name': 'isQqQrCodeShown'}]
# for i in range(0, len(add_cookie)):
#     driver.add_cookie(add_cookie[i])
#
# driver.get(base_url)
#
# print(len(add_cookie))


f = open('cookie.txt', 'r')
fc = f.read()
print(fc)
# a = ['%s' % fc]
#
# print(len(a))
# print(a)

x = [1]
y = {1, '\'j\': \'1\''}
x.append(y)
print(x)