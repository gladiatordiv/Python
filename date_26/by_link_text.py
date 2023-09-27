import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        link_element = driver.find_element(By.LINK_TEXT, "Yatra for Business")
        link_element.click() 
        time.sleep(4)

findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()