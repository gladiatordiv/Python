import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
class DemoMouseOver():
    def demo_mouse_events(self):
        driver=webdriver.Chrome()
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        # Right click
        achains=ActionChains(driver)
        elem1=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
        copyele=driver.find_element(By.XPATH,"//span[normalize-space()='Copy']")
        achains.context_click(elem1).perform()
        time.sleep(3)
        copyele.click()
        time.sleep(3)
drightclick=DemoMouseOver()
drightclick.demo_mouse_events()