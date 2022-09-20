import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# 如果有的按钮需要点击两次才能生效，那就需要自己进行封装
# 期望条件的设计：需求，一直点击按钮，直到下一个页面的出现
#输入1、点击的目标按钮，输入二，下一个页面的某个元素
def muti_click(target_ele,next_ele):

    def _inner(driver):
        driver.find_element(*target_ele).click()
        #第一种结果为找到，return的内容为webelement对象
        #第二种没有找到，driver.find_element(*next_ele)的代码报错，但被until中的异常捕获逻辑捕获异常，继续循环
        return driver.find_element(*next_ele)

    return  _inner

def wait_until_click_twice():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study/frame")
    WebDriverWait(driver, 10).until(muti_click(
        (By.ID, 'primary_btn'),
        (By.XPATH,"/html/body/div[2]/div/div[1]/div/span")
        ))
    driver.find_element(By.ID, "primary_btn").click()
    time.sleep(3)

if __name__ == '__main__':
    wait_until_click_twice()