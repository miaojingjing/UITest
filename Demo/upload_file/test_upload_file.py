import time

from selenium.webdriver.common.by import By

from base import Base


class Test_UPLoad_File(Base):
    def test_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element(By.CSS_SELECTOR,".st_camera_off").click()
        self.driver.find_element(By.ID,"uploadImg").send_keys("d:\Documents and Settings\\60055202\桌面\logo.png")
        time.sleep(3)

    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
