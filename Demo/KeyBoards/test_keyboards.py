import sys
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestKeyboard:
    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_shift(self):
        '''
        1、访问https://ceshiren.com/
        2、点击搜素按钮
        3、输入收缩的内容，输入的同时按住shift键
        '''
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.ID,"search-button").click()
        ele=self.driver.find_element(By.ID,"search-term")
        ActionChains(self.driver).key_down(Keys.SHIFT,ele).send_keys("selenium").perform()
        time.sleep(2)

    def test_enter(self):
        self.driver.get("https://www.sogou.com/")
        self.driver.find_element(By.ID,"query").send_keys("你好")
        #第一种回车方式
        # self.driver.find_element(By.ID, "query").send_keys(Keys.ENTER)
        # time.sleep(2)
        # 第二种回车方式
        ActionChains(self.driver).key_down(Keys.ENTER).perform()
        time.sleep(2)

    def test_copy_and_paste(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.ID,"search-button").click()
        ele=self.driver.find_element(By.ID,"search-term")
        # 判断操作系统是否为mac ,如果是mac ,则返回command键位，如果是windows,则返回control键位
        command_control = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
        ActionChains(self.driver).key_down(Keys.SHIFT,ele).send_keys("selenium!").key_down(Keys.ARROW_LEFT).key_down(command_control).send_keys("xvvv").key_up(command_control).perform()
        time.sleep(2)