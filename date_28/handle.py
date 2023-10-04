from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")
dropdown_element = driver.find_element(By.ID,"your_dropdown_id")

dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Option Text")
dropdown.select_by_index(1)  
dropdown.select_by_value("option_value")
selected_option = dropdown.first_selected_option
print("Selected option:", selected_option.text)
driver.quit()
