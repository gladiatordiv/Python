import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Demodragdrop():
    def drag_drop(self):
        driver=webdriver.Chrome()
        driver.get("https://jqueryui.com/droppable/")
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
        elem1=driver.find_element(By.ID,"draggable")
        elem2=driver.find_element(By.ID,"droppable")
        action = ActionChains(driver)
        action.drag_and_drop(elem1, elem2).perform()
        
        time.sleep(4)

dd=Demodragdrop()
dd.drag_drop()
