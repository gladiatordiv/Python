import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class DemoSliders():
    def sliders(self):
        driver = webdriver.Chrome()
        driver.get("https://www.snapdeal.com/products/mobiles-cables-chargers?sort=plrty")
        left_handle = driver.find_element(By.XPATH, "//a[@class='price-slider-scroll left-handle ui-slider-handle ui-state-default ui-corner-all hashAdded ui-state-hover ui-state-focus']")
        right_handle = driver.find_element(By.XPATH, "//a[@class='price-slider-scroll right-handle ui-slider-handle ui-state-default ui-corner-all hashAdded ui-state-hover ui-state-focus']")
        actions = ActionChains(driver)
        actions.move_to_element(left_handle).pause(1).click_and_hold(left_handle).move_by_offset(80, 0).release().perform()
        time.sleep(4)
slider = DemoSliders()
slider.sliders()
