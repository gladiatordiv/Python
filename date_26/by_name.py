import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        link_element = driver.find_element(By.CLASS_NAME, "email-login-box")
        link_element.send_keys('test@rcvacademy.com')
        time.sleep(4)

findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()