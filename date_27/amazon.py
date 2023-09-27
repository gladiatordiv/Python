from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/-/hi/ap/signin?openid.pape.max_auth_age=3600&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fspr%2Freturns%2Fgift&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_psr_desktop_in&openid.mode=checkid_setup&language=en_IN&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
email_phonenumber= driver.find_element(By.XPATH, "//input[@id='ap_email']")
email_phonenumber.send_keys("divyabwr30702@gmail.com")
password = driver.find_element(By.XPATH,"//input[@id='ap_password']")
password.send_keys("divyachauhan")
sign_in=driver.find_element(By.XPATH,"//input[@id='signInSubmit']")
sign_in.click()
time.sleep(10)
driver.quit()