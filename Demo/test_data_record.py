import time

from selenium.webdriver.common.by import By

from base import Base
from data_record.log_utils import logger


class TestDataRecord(Base):
    def test_record_logs(self):
        search_content="霍格沃兹测试开发"
        self.driver.get("https://www.sogou.com/")
        self.driver.find_element(By.ID,"query").send_keys(search_content)
        logger.debug(f"搜索的内容为{search_content}")
        self.driver.find_element(By.ID,"stb").click()
        self.driver.implicitly_wait(3)
        #获取搜索结果，对应测试用例的实际结果
        search_result = self.driver.find_element(By.CSS_SELECTOR, "em")
        print(search_result.text)
        logger.info(f"实际结果为{search_result.text},预期结果为{search_content}")
        assert search_result.text == search_content

    def test_screen_shot_data_record(self):
        search_content="霍格沃兹测试开发"
        self.driver.get("https://www.sogou.com/")
        self.driver.find_element(By.ID,"query").send_keys(search_content)
        logger.debug(f"搜索的内容为{search_content}")
        self.driver.find_element(By.ID,"stb").click()
        self.driver.implicitly_wait(3)
        # 获取搜索结果，对应测试用例的实际结果
        search_result = self.driver.find_element(By.CSS_SELECTOR, "em")
        print(search_result.text)
        logger.info(f"实际结果为{search_result.text},预期结果为{search_content}")
        # 在断言之前添加截图
        self.driver.save_screenshot("res.png")
        assert search_result.text == search_content

    # 现象，：产生了 no such element的错误
    # 解决方案：在报错的代码行之前打印page_source,确定定位的元素没有问题，主要用于调试
    def test_page_source_data_record(self):
        search_content="霍格沃兹测试开发"
        self.driver.get("https://www.sogou.com/")
        # 获取page_source
        with open("record2.html","w",encoding="u8") as f:
            f.write(self.driver.page_source)
        self.driver.find_element(By.ID,"query1").send_keys(search_content)




