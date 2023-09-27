import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class Demoseleniumlearning():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.redbus.in")
        text = driver.find_element(By.XPATH, "//h2[@class='AboutUs__Heading-w9osof-3 lmIkvI']").text

        print(text)
        time.sleep(2)

findbyid = Demoseleniumlearning()
findbyid.locate_by_id_demo()