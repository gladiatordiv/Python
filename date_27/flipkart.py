from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/account/login")
email_phonenumber = driver.find_element(By.XPATH, "//input[@class='_2IX_2- VJZDxU']")
email_phonenumber.send_keys("7014330870")
request_otp = driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")
request_otp.click() 
time.sleep(10)
verify_input = driver.find_element(By.XPATH, '//div[@class="HSKgdN"]')
verify_input.send_keys("749198")
verify = driver.find_element(By.xpath("//button[normalize-space()='Verify' and @class='_2IX_2- VJZDxU']"))
verify.click()
driver.quit()