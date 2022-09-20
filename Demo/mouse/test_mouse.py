import sys
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestKeyboard:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_double_click(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study/frame")
        ele=self.driver.find_element(By.ID,"primary_btn")
        # 调用双击的方法，传入被双击的元素
        ActionChains(self.driver).double_click(ele).perform()
        time.sleep(2)

    def test_drog_and_drop(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study/action_chains")
        # 获取启始元素的位置
        start_ele=self.driver.find_element(By.ID,"item1")
        # 获取目标元素的位置
        target_ele=self.driver.find_element(By.ID, "item3")
        #实现拖拽操作
        ActionChains(self.driver).drag_and_drop(start_ele,target_ele).perform()
        time.sleep(2)

    def test_move_to_element(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study/action_chains2")
        ele = self.driver.find_element(By.CSS_SELECTOR, ".menu")
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(2)
        # 选择里面的定位
        ele_option=self.driver.find_element(By.XPATH,"//*[text()=' 管理班 ']").click()
        time.sleep(2)

    def test_scroll_to_element(self):
        self.driver.get("https://blog.csdn.net/yuer011/article/details/117300919")
        ele = self.driver.find_element(By.XPATH,'//*[text()="专栏目录"]')
        ActionChains(self.driver).scroll_to_element(ele).perform()
        time.sleep(2)
    def test_scroll_to_XY(self):
        self.driver.get("https://blog.csdn.net/yuer011/article/details/117300919")
        ActionChains(self.driver).scroll_by_amount(0,3000).perform()
        time.sleep(2)
