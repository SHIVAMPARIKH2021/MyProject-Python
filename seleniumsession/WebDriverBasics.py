from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\shiva\\eclipse-workspace\\Myproject\\chromedriver.exe")
driver.get("http://www.google.com")
print(driver.title)


driver.find_element(By.NAME,"q").send_keys('Python Frameworks lists')
driver.implicitly_wait(5)
list = driver.find_elements(By.CSS_SELECTOR,'ul.erkvQe li span')
print(len(list))

for elementlist in list:
    print(elementlist.text)
    if elementlist.text == "python framework list for automation":
        elementlist.click()
        break
driver.quit()
