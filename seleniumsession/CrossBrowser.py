from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class CrossBrowser:
    browser_name = "chrome"

    def setup(self, browser_name):
        self.browser_name = browser_name
        if browser_name == "chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser_name == "edge":
            driver = webdriver.Edge(EdgeChromiumDriverManager().instaLL())
        elif browser_name == "firefox":
            driver = webdriver.Firefox(service=GeckoDriverManager().install())
        else:
            print("please pass the browser_name: " + browser_name)

        driver.implicitly_wait(5)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        page_title = driver.title
        return driver

