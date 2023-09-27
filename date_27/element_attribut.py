import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class Demoseleniumlearning():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://yatra.com")
        attr_value = driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("value")
        print(attr_value)
        time.sleep(2)

attobj = Demoseleniumlearning()
attobj.locate_by_id_demo()