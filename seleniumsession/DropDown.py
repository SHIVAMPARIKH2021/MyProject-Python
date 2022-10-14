from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


class DropDown:

    @staticmethod
    def select_drop_down(locator_xpath_elements, value_from_dropdown):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.amazon.ca/")
        driver.maximize_window()
        driver.refresh()
        drop_down_list = driver.find_elements(By.XPATH, str(locator_xpath_elements))
        for element in drop_down_list:
            print(element.text)
            driver.implicitly_wait(15)
            if element.text == str(value_from_dropdown):
                element.click()
                driver.close()
                break

    @staticmethod
    def select_method(locator_xpath, input_value):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.amazon.ca/")
        driver.maximize_window()
        driver.refresh()
        driver.implicitly_wait(15)
        select = Select(driver.find_element(By.XPATH, str(locator_xpath)))
        if type(input_value) == "str":
            parameter_index = select.select_by_value(str(input_value))
            print(parameter_index)
        elif type(input_value) == "int":
            parameter_value = select.select_by_index(int(input_value))
            print(parameter_value)
        driver.close()
        return print(select.is_multiple)

    select_method("//select[@id='searchDropdownBox' and @name='url']", 4)

    select_drop_down("//select[@id='searchDropdownBox']/option", "Automotive")
