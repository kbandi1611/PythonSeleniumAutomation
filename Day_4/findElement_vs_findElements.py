import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#################find_element######################### -- Returns single web element


# 1)Locator matching with single web element
element = driver.find_element(By.XPATH, '//*[@id="small-searchterms"]')
element.send_keys("Apple Macbook Pro 13-inc")
driver.find_element(By.XPATH, '//*[@id="small-search-box-form"]/button').click()
time.sleep(5)

# 2)Locator matching with multiple web elements
# element = driver.find_element(By.XPATH, '//div[@class="footer"]//a')
# print(element.text)  # prints first link from the footer section

# 3)If element is not available then it throws NoSuchElementException
# login_element = driver.find_element(By.LINK_TEXT, 'Log')
# time.sleep(5)
# login_element.click()
# time.sleep(5)

########################find_elements################# -- Returns multiple web elements

# 1)Locator matching with single web element
# element = driver.find_elements(By.XPATH, '//*[@id="small-searchterms"]')
# print(len(element))  # 1
# element[0].send_keys('Apple Macbook Pro 13')
# time.sleep(3)

# 2)Locator matching with multiple web elements
# element = driver.find_elements(By.XPATH, '//div[@class="footer"]//a')
# print(len(element))  # 23
# # print(element[0].text) #Sitemap
# for i in element:
#     print(i.text)

# 3)If element is not available
# login_element = driver.find_elements(By.LINK_TEXT, 'Log')
# print(len(login_element))
