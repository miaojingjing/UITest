import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def wait_until():
    driver=webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study/frame")
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#success_btn')))
    driver.find_element(By.CSS_SELECTOR,"#success_btn").click()
    time.sleep(3)
if __name__ == '__main__':
    wait_until()
    #driver="aaa"
    # def fake_confitions(driver):
    #     print("当前时间为",time.time())
        # until 传入的参数是一个函数对象，不是函数的调用
    # 错误的调用示范
    # WebDriverWait(driver,10,2).until(fake_confitions())
    # WebDriverWait(driver, 10, 2).until(fake_confitions,"测试开发")