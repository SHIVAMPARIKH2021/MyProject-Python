from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://spicejet.com")
elem_add_ons = driver.find_element(By.XPATH, "//div[text()='Add-ons']")
action = ActionChains(driver)
action.move_to_element(elem_add_ons).perform()
new_ele = driver.find_element(By.XPATH, "//div[text()='Spice Assurance']")
action.move_to_element(new_ele).perform()
new_ele.click()
time.sleep(3)
driver.close()


