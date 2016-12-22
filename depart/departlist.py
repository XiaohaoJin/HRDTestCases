# coding: utf-8

from selenium import webdriver
from login import login
from time import sleep
from random import choice
from tools import random_phoneNum
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class DepartListTestCase(unittest.TestCase):

    tu = login.LoginTestCase()
    wd = tu.test_login()

    def test_depart_list(self):
        try:
            print('try depart')
            sleep(2)
            self.wd.find_element_by_link_text(u"员工管理").click()
            self.wd.implicitly_wait(10)
            sleep(1)
            print("员工管理")


            # 添加部门
            # self.wd.find_element_by_xpath("//div[@id='container']/div[2]/img[2]").click()
            # self.wd.find_element_by_css_selector("#402881dc52fd4b190152fd51fee60001 > div.node-topo > div.row.node-tbottom > a.col-xs-6.tbottom-item > span.glyphicon.glyphicon-plus").click()
            # sleep(1)
            # self.wd.find_element_by_id("depart_name").clear()
            # self.wd.find_element_by_id("depart_name").send_keys(u"技术部")
            # sleep(1)
            # self.wd.find_element_by_xpath("(//button[@type='button'])[3]").click()
            # self.wd.implicitly_wait(2)
            # sleep(2)
            #删除部门
            # self.wd.find_element_by_id("depart_name").clear()
            # self.wd.find_element_by_id("depart_name").send_keys(u"技术部")
            # sleep(2)
            # self.wd.find_element_by_css_selector("span.glyphicon.glyphicon-trash").click()
            # self.assertEqual(u"确定要删除此部门？", self.close_alert_and_get_its_text())
            # self.assertEqual(u"删除成功！", self.close_alert_and_get_its_text())


            # self.wd.find_element_by_link_text(u"员工列表").click()
            # self.wd.implicitly_wait(30)
            # print("员工列表")
            # sleep(2)
            #
            # self.wd.find_element_by_link_text(u"员工画像").click()
            # self.wd.implicitly_wait(30)
            # print("员工画像")
            # sleep(2)
            #
            # self.wd.find_element_by_link_text(u"身份审核").click()
            # self.wd.implicitly_wait(30)
            # print("身份审核")
            # sleep(2)



            self.wd.find_element_by_link_text(u"添加员工").click()
            self.wd.implicitly_wait(10)
            sleep(1)
            print("添加员工")

            # WebDriverWait(self.wd, 5).until(EC.alert_is_present(), 'Error: 没有找到弹窗')
            self.input_info(self)

        except:
            print('except depart')
            sleep(3)
            self.wd.quit()
        finally:
            print('finally depart')

    # 添加员工信息，输入员工姓名和手机号测试
    def input_info(self):
        # telphone = random_phoneNum.random_PhoneNumber(self)
        telphone = '18911958679'
        name = '测试名'
        print(telphone)

        self.wd.find_element_by_id("user_name").clear()
        self.wd.find_element_by_id("user_name").send_keys(name)

        self.wd.find_element_by_id("user_phone").clear()
        self.wd.find_element_by_id("user_phone").send_keys(telphone)
        self.wd.find_element_by_css_selector("button.botton.green_bg").click()
        self.check_phone_error()

    # 检查手机号是否重复
    def check_phone_error(self):
        try:
            # 等待弹窗出现，超时时间5秒
            WebDriverWait(self.wd, 5).until(EC.alert_is_present(), 'Error: 没有找到弹窗')
            alert = self.wd.switch_to_alert() # 切换到弹窗
            if alert.text == "该手机号已经存在！":
                print(u"该手机号已经存在！")
                sleep(2)
                alert.accept() # 点击弹窗中的确定按钮

            self.input_info()
        except:
            print('成功添加一位员工！')


if __name__ == '__main__':
    dep = DepartListTestCase()
    dep.test_depart_list()

    # dep.wd.quit()
