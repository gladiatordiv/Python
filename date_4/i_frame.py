import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Demoiframe():
    def demoframe(self):
        driver=webdriver.Chrome()
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
        '''driver.switch_to.frame(0)
        driver.find_element(By.XPATH,"//a[@id='cert_navbtn']").click()'''
        time.sleep(4)
diframe=Demoiframe()
diframe.demoframe