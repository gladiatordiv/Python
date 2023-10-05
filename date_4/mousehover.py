import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
class DemoMouseOver():
    def demo_mouse_events(self):
        driver=webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        morebutton=driver.find_element(By.XPATH,"//span[@class='more-arr']")
        
        achains=ActionChains(driver)
        achains.move_to_element(morebutton)
        driver.find_element(By.XPATH,"//span[normalize-space()='Luxury Trains']").click()
        time.sleep(3)
dmouse=DemoMouseOver()
dmouse.demo_mouse_events()