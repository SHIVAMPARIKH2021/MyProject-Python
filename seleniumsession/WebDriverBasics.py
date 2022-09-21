from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\shiva\\eclipse-workspace\\Myproject\\chromedriver.exe")
driver.get("http://www.google.com")
print(driver.title)