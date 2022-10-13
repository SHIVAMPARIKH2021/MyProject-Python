import webdriver_manager.chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from seleniumsession.CrossBrowser import CrossBrowser


class Locators:
    cross_browser = CrossBrowser()
    locator_object = cross_browser.setup("chrome")
    print(locator_object.title)

    # Variables of type 'WebElement' are created
    my_info_url = locator_object.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()
    first_name = locator_object.find_element(By.NAME, "firstName")
    middle_name = locator_object.find_element(By.NAME, "middleName")
    last_name = locator_object.find_element(By.NAME, "lastName")
    nick_name = locator_object.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input")
    employee_id = locator_object.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input")


class SubLocators(Locators):
    sub_locators = Locators()

    # Executing the WebDriver methods with the help of variable of parent class 'Locators'
    sub_locators.first_name.clear()
    sub_locators.first_name.send_keys("Jonathan")
    sub_locators.middle_name.clear()
    sub_locators.middle_name.send_keys("David")
    sub_locators.last_name.clear()
    sub_locators.last_name.send_keys("Smith")
    sub_locators.nick_name.send_keys("Jonny")
    sub_locators.employee_id.clear()
    sub_locators.employee_id.send_keys("00400")
    sub_locators.locator_object.quit()
