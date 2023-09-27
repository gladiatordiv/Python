import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class Demoseleniumlearning():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        driver.fullscreen_window()
        elem=driver.find_element(By.XPATH,"//input[@id='doi0']")
        elem.click()
        time.sleep(5)
demo=Demoseleniumlearning()
demo.locate_by_id_demo()