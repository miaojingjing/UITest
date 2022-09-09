from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def element_wait():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    # 不加等待，可能会因为网速等原因产生报错
    # ======================报错：no such element: Unable to locate element===================
    # ======================原因：页面未加载完成，就去查找元素，但此时这个给元素还没有加载出来===================
    # ======================解决方案：直接等待，在no such element: Unable to locate element报错之前添加强制等待，等待页面渲染完成。
    # 如果没有报错，证明是页面渲染速度导致的问题，如果添加了强制等待还报错，那么可能是别的问题，比如定位错误。
    # time.sleep(3)
    # ************* 隐式等待
    # 强制等待的问题：1、不确定页面的加载时间，可能会因为等待时间过长，而影响用例的执行效率
    # ----------------2、不确定页面的加载时间，可能会因为等待时间过短，而导致代码依然没有找到元素报错
    # 设置一个等待时间，轮询查找（默认0.5s）元素是否出现，如果没有出现就抛出异常
    # 使用方法：在代码一开始运行的时候就添加隐式等待的配置，注意，隐式等待是全局生效，所有，在所有的find_element动作之前就执行此代码
    driver.implicitly_wait(3)
    driver.find_element(By.ID, "kw")
    driver.find_element(By.ID, "su")

    # 显示等待 element  not interactable


if __name__ == '__main__':
    element_wait()
