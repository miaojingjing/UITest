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

