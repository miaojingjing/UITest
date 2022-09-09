from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 8 种定位方式
def web_locate():
    # 首先需要实例化driver对象，Chrome()一定要加括号
    driver = webdriver.Chrome()
    # 打开一个网页
    driver.get("https://vip.ceshiren.com/#/ui_study/locate")
    # # id 定位,第一个参数传递定位方式，第二个参数传递定位元素
    # web_element_id = driver.find_element(By.ID, "located_id")
    # print(web_element_id)
    # # name 定位
    # # 如果没有报错，证明元素找到了
    # web_element_name= driver.find_element(By.NAME, "located_name")
    # print(web_element_name)
    #
    # # CSS_SELECTOR 定位
    # web_element_css=driver.find_element(By.CSS_SELECTOR,"#app > div > section > section > main > div > div.box > div:nth-child(3) > button")
    # print(web_element_css)
    # # xpath 定位
    # web_element_xpath=driver.find_element(By.XPATH,"//*[@id='app']/div/section/section/main/div/div[1]/div[3]/button")
    # print(web_element_xpath)

    # 链接文本的方式 （1）元素一定是a 标签 （2）输入的元素为标签内的文本
    web_element_linkText = driver.find_element(By.LINK_TEXT,"元素定位").click()

    sleep(5)
    #部分链接文字
    web_element_plinkText = driver.find_element(By.PARTIAL_LINK_TEXT, "partial").click()


if __name__ == '__main__':
    web_locate()
