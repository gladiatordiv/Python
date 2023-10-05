import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class DemoJspopus():
    def demo_js_alerts(self):
        driver=webdriver.Chrome()
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")
        #accept alert
        # driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        # time.sleep(6)
        # driver.switch_to.alert.accept()
        # time.sleep(2)
        # dismiss alert
        # driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        # time.sleep(2)
        # driver.switch_to.alert.accept()
        # time.sleep(2)
        # send test in alert
        driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.send_keys("Divya Chauhan")
        driver.switch_to.alert.accept()
        time.sleep(2)

dpopup=DemoJspopus()
dpopup.demo_js_alerts()
