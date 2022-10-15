from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
right_clickable_elem = driver.find_element(By.XPATH, "//span[text()='right click me']")
action = ActionChains(driver)
action.context_click(right_clickable_elem).perform()

elems_list = driver.find_elements(By.CSS_SELECTOR, "li.context-menu-item.context-menu-icon")


def right_Click(value):
    for clicked_list in elems_list:
        print(clicked_list.text)
        if clicked_list.text == value:
            clicked_list.click()
            driver.switch_to.alert.accept()
            driver.close()


right_Click("Quit")