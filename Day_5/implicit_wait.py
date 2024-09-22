import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

driver.get("https://www.google.com")
driver.maximize_window()
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys("Selenium")
search_box.submit()

driver.find_element(By.XPATH, '//h3[text()="Selenium"]').click()
time.sleep(3)
