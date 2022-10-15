import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class JQueryDropDown:

    def select_dropdown(self, ALL_VALUE, item_list, value_to_enter):
        if ALL_VALUE[0] != 'all':
            for elems in item_list:
                print(elems.text)
                for k in range(len(value_to_enter)):
                    if elems.text == value_to_enter[k]:
                        elems.click()
                        break
        else:
            try:
                for elems in item_list:
                    elems.click()
            except Exception as e:
                print(e)


''' Execution of method:'''

# Initialising the 'driver' 

driver = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(2)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.maximize_window()
driver.find_element(By.ID, 'justAnInputBox').click()

# Declaring the input parameters to execute the method

items = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
values = ['choice 1', 'choice 4', 'choice 5']
ALL_VALUES = [0,'all']

# Creating an object to execute the method
# Constructor will be invoked as the object will be created

jQ_dropdown = JQueryDropDown()
jQ_dropdown.select_dropdown(ALL_VALUES, items, values)
driver.close()

# ALL_VALUES,items,values
