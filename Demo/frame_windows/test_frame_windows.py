import sys
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base import Base


class TestKeyboard(Base):

    def test_windows(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.LINK_TEXT,"登录").click()
        # 打印当前页面的窗口句柄
        print(self.driver.current_window_handle)
        self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        print(self.driver.window_handles)
        windows=self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element(By.ID,'TANGRAM__PSP_4__userName').send_keys("sss")

        time.sleep(2)
        self.driver.switch_to.window(windows[0])
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__userName').send_keys("aaa")
        time.sleep(3)

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element(By.ID, "draggable").text)
        self.driver.switch_to.default_content()
        print(self.driver.find_element(By.ID, "submitBTN").text)
        time.sleep(3)

