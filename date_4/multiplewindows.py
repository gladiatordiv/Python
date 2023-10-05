import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class DemoMultipleWindows():
    def demo_windows(self):
        driver=webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        parent_handle=driver.current_window_handle
        print(parent_handle)
        element = driver.find_element(By.XPATH, "//a[@class='offerLobUrl']")
        element.click()
        all_handles=driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH, "//a[@href='https://www.yatra.com/prime']//span[@class='wfull offer-content anim']//span[@class='details wfull bxs']//span[@class='flL view mt10']//span[@class='view-btn flR anim'][normalize-space()='View Details']")
                time.sleep(4)
                driver.close()
                time.sleep(5)
                break
        driver.switch_to.window(parent_handle)
        driver.find_element(By.XPATH, "//a[@class='offerLobUrl']")

dmultiplewindows=DemoMultipleWindows()
dmultiplewindows.demo_windows()
