import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#元素操作
# def element_interaction():
#     driver=webdriver.Chrome()
#     driver.get("https://www.baidu.com")
#     driver.find_element(By.ID,"kw").send_keys("霍格沃兹测试开发")
#     time.sleep(2)
#     driver.find_element(By.ID,"kw").clear()
#     time.sleep(2)
#     driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试开发")
#     time.sleep(2)
#     driver.find_element(By.ID, "su").click()
#     time.sleep(2)

#获取元素属性
def element_get_attr():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study/frame")
    webele=driver.find_element(By.LINK_TEXT,"元素定位")
    #断点打在想看的对象的下一行
    print(webele)
    #获取元素的文本信息，不是所有元素都有文本
    print(webele.text)
    #获取元素的属性信息
    res=webele.get_attribute("class")
    print(res)

if __name__ == '__main__':
    element_get_attr()

