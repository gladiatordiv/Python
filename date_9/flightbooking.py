from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
def open_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def is_logged_in(driver):
    driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
    try:
        driver.find_element(By.XPATH, "//li[normalize-space()='Logout']")
        return True
    except NoSuchElementException:
        return False

def login(driver):
    if not is_logged_in(driver):
        time.sleep(3)
        driver.get("https://www.makemytrip.com/flights/?gclid=CjwKCAjwyY6pBhA9EiwAMzmfwY1O-9isH0KX-6P4qtwlu0h33M5rVsTdSo2kOoYS3f4e2xdUSpzUXhoClwsQAvD_BwE:G:s")
        time.sleep(3)
        login_button = driver.find_element(By.XPATH, "//div[@class='nsm7Bb-HzV7m-LgbsSe-Bz112c']")
        login_button.click()
        time.sleep(4)
        email_input = driver.find_element(By.XPATH, "//div[normalize-space()='Divya Chauhan']")
        email_input.click()
        time.sleep(2)
        if is_logged_in(driver):
            print("Logged in successfully")
        else:
            print("Login failed")
    else:
        print("Already logged in")

try:
    driver = open_browser()
    login(driver)
finally:
    driver.quit()
