import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoSS():
    def demoss(self):
        driver=webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

        continuedemo=driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
        continuedemo.screenshot("./test.png")
        continuedemo.click()
        time.sleep(2)
        driver.get_screenshot_as_file("C:/Users/ASUS/Desktop/Celebal(Python)/date_29/error.png")
        driver.save_screenshot(".test1.png")
Demoss=DemoSS()
Demoss.demoss()