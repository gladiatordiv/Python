import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class Demoseleniumlearning():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        elem=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(elem)
        a=driver.find_element(By.XPATH,"//button[@class='ws-btn w3-hover-black w3-dark-grey']")
        a.click()
        elem1=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(elem1)
demo=Demoseleniumlearning()
demo.locate_by_id_demo()