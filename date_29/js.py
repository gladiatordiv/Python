import time
from selenium import webdriver
# from webdriver_manager.chrome import Select

class Demo():
    def demo_js(self):
        driver=webdriver.Chrome()
        driver.get("https://training.rcvacademy.com/")
        driver.execute_script("window.open('https://training.rcvacademy.com/','_self');")
        time.sleep(4)
        demo_element=driver.execute_script("return document.getElementsByTagName('p')[13];")
        driver.execute_script("arguments[0].click();",demo_element)
demojs=Demo()

demojs.demo_js()