from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# 
def open_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
def wait_and_select_dropdown(driver, xpath, value):
    try:
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        dropdown = Select(element)
        dropdown.select_by_value(value)
    except Exception as e:
        print(f"Error: {e}")
def registration_form():
    driver = open_browser()
    driver.get("https://nxtgenaiacademy.com/demo-site/")
    
    driver.find_element(By.XPATH, "//input[@id='vfb-5']").send_keys("Divya")
    driver.find_element(By.XPATH, "//input[@id='vfb-7']").send_keys("Chauhan")
    gender = driver.find_element(By.XPATH, "//input[@id='vfb-31-2']")
    if not gender.is_selected():
        gender.click()
    driver.find_element(By.XPATH, "//input[@id='vfb-13-address']").send_keys("Beawar")
    driver.find_element(By.XPATH, "//input[@id='vfb-13-state']").send_keys("Rajasthan")
    driver.find_element(By.XPATH, "//input[@id='vfb-13-city']").send_keys("Beawar")
    
    country_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='vfb-13-country']"))
    country_dropdown.select_by_visible_text("India")
    
    driver.find_element(By.XPATH, "//input[@id='vfb-14']").send_keys("divyabwr30702@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='vfb-18']").send_keys("08/10/2023")
    wait_and_select_dropdown(driver, "//span[@class='select2 select2-container select2-container--default select2-container--below select2-container--focus']//span[@role='presentation']", '11')
    wait_and_select_dropdown(driver, "//span[@class='select2 select2-container select2-container--default select2-container--focus']//span[@role='presentation']", '11')
    driver.find_element(By.XPATH, "//input[@id='vfb-19']").send_keys("7014330870")
    course_1 = driver.find_element(By.XPATH, "//input[@id='vfb-20-0']")
    if not course_1.is_selected():
        course_1.click()
    course_2 = driver.find_element(By.XPATH, "//input[@id='vfb-20-3']")
    if not course_2.is_selected():
        course_2.click()
    
    driver.find_element(By.XPATH, "//textarea[@id='vfb-23']").send_keys("ok")
    
    extracting_text = driver.find_element(By.XPATH, "//label[normalize-space()='Example: 99']")
    text = extracting_text.text.strip()
    if text.startswith("Example:"):
        number_str = text.split(":")[1].strip()
        if number_str.isdigit():
            number = int(number_str)
            driver.find_element(By.XPATH, "//input[@id='vfb-3']").send_keys(number)
    submit = driver.find_element(By.XPATH, "//input[@id='vfb-4']")
    submit.click()
    time.sleep(3)
    
    if "Registration Form is Successfully Submitted" in driver.page_source:
        print("Successfully Submitted")
    
    driver.quit()
registration_form()
