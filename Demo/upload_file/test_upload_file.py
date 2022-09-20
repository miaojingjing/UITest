import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base import Base


class Test_UPLoad_File(Base):
    def test_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element(By.CSS_SELECTOR,".st_camera_off").click()
        self.driver.find_element(By.ID,"uploadImg").send_keys("d:\Documents and Settings\\60055202\桌面\logo.png")
        time.sleep(3)

    def test_alert(self):
        '''
        1|打开网页：https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
        操作窗口右侧的页面，将元素1拖拽到元素2
        这时候会有一个alert弹框，点击确定
        然后点击运行
        关闭页面
        '''
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        ele1=self.driver.find_element(By.ID,"draggable")
        ele2=self.driver.find_element(By.ID,"droppable")
        ActionChains(self.driver).drag_and_drop(ele1, ele2).perform()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        print("点击确认")
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID,"submitBTN").click()
        time.sleep(3)

