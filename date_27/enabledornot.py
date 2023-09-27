import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class Demoseleniumlearning():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://training.openspan.com/login")
        enabled_ornot = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(enabled_ornot)
        driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys("testing")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("testing143")
        enabled_ornot1 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(enabled_ornot1)
findbyid = Demoseleniumlearning()
findbyid.locate_by_id_demo()