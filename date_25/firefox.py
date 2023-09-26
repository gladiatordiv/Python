from selenium import webdriver
driver_path = "C:\browserdrivers\geckodriver.exe"
driver = webdriver.Firefox(executable_path=driver_path)
driver.get('https://www.google.com/')
driver.quit()
