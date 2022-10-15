import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://demoqa.com/droppable")
time.sleep(3)
print(driver.title)
source_elem = driver.find_element(By.ID, "draggable")
target_elem = driver.find_element(By.ID, "droppable")


action = ActionChains(driver)

flag = False

if flag == True:
    action.drag_and_drop(source_elem, target_elem).perform()
else:
    action.click_and_hold(source_elem).move_to_element(target_elem).release(target_elem).perform()

driver.close()
