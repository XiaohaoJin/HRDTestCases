# coding: utf-8

from selenium import webdriver
from login import login
from time import sleep

class DepartListTestCase():

    tu = login.LoginTestCase()
    wd = tu.test_login()
    sleep(1)
    # urlDepart = 'http://www.bycoming.com/hrd/depart_list.do'

    def test_depart_list(self):
        try:
            print('try depart')
            print(self.wd.current_url)
            sleep(1)
            self.wd.find_element_by_link_text(u"员工管理").click()
            self.wd.find_element_by_xpath("//div[@id='container']/div[2]/img").click()
            self.wd.find_element_by_xpath("//div[@id='container']/div[2]/img[2]").click()
            self.wd.find_element_by_xpath("//div[@id='container']/div[2]/img[3]").click()
            self.wd.find_element_by_xpath("//div[@id='container']/div[2]/img[4]").click()
            self.wd.find_element_by_xpath("//div[@id='container']/div[2]/img[5]").click()
            self.wd.find_element_by_xpath("//div[@id='container']/div[2]/img[6]").click()
            self.wd.find_element_by_xpath("//div[@id='container']/div[2]/img[7]").click()
            self.wd.find_element_by_xpath("//div[@id='container']/div[2]/img[8]").click()
            self.wd.find_element_by_xpath("//div[@id='container']/div[2]/img[9]").click()
            self.wd.find_element_by_xpath("//div[@id='container']/div[2]/img[9]").click()
            self.wd.find_element_by_xpath("//div[@id='sidebar']/ul/li[2]/a/span").click()

            print('执行完毕')
        except:
            print('except depart')

        finally:
            print('finally depart')

if __name__ == '__main__':
    dep = DepartListTestCase()
    dep.test_depart_list()
    sleep(2)
    dep.wd.quit()
