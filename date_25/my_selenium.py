from selenium import webdriver
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)
driver.get('https://www.google.com/')