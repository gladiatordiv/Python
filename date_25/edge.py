from selenium import webdriver
driver=webdriver.Edge(executable_path="C:\browerdrivers\msedgedriver.exe")
driver.get("https://www.google.com")
driver.maximize_window()
print(driver.title)