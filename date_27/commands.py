import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class Demoseleniumlearning():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/social/common/yatra/signin.htm")
        link_element = driver.find_element(By.CLASS_NAME, 'email-login-box')
        link_element.send_keys('rcv@rcvacademy.com')
        time.sleep(4)

findbyid = Demoseleniumlearning()
findbyid.locate_by_id_demo()