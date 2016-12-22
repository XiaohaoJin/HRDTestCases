# coding: "UTF-8"

from selenium import webdriver
from time import sleep
from tools import captcha


class LoginTestCase():

    wd = webdriver.Firefox()
    urlLogin = 'http://www.bycoming.com/hrd/hrd_login.do'
    account = '13333333334'
    pwd = '123456'

    def test_login(self):
        try:
            print('try login')
            self.wd.get(self.urlLogin)

            self.wd.find_element_by_id('user_name').send_keys(self.account)
            self.wd.find_element_by_id('user_pass').send_keys(self.pwd)

            self.input_captcha_login() # 输入验证码并登录
        except:
            print('expect login')
        finally:
            print('finally login')
            return self.wd

    def input_captcha_login(self):
        sleep(1)
        txt = captcha.captcha_text(self.wd, 'img_code') # 获取验证码内容
        print(txt)
        element = self.wd.find_element_by_id('user_code') # 获取验证码输入框
        element.clear() # 清空验证码输入框
        element.send_keys(txt) # 输入验证码
        self.wd.find_element_by_id('login_button').click() # 点击登录
        self.check_captcha_error() # 检查是否有验证码错误问题

    # 如果验证码错误，则重新获取验证码再次登录
    def check_captcha_error(self):
        if self.urlLogin == self.wd.current_url:
            self.wd.find_element_by_id('img_code').click() # 刷新验证码
            self.input_captcha_login() # 输入验证码并登录
            self.wd.implicitly_wait(10)
            print('验证码错误，已重新输入')


if '__main__' == __name__:
    tc = LoginTestCase()
    tc.test_login()
    sleep(5)
    tc.wd.quit()