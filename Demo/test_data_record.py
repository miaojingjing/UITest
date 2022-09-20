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

