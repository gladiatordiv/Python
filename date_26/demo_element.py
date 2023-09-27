import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver=webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        element = driver.find_element('id', 'login-input')
        element.send_keys('test@test.com')
        time.sleep(4)
findbyid=DemoFindElementByID()
findbyid.locate_by_id_demo()