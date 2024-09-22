import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)
# driver.get("https://the-internet.herokuapp.com/login")
driver.get("http://tomsmith:SuperSecretPassword!@the-internet.herokuapp.com/login")
driver.find_element(By.XPATH, '//*[@id="login"]/button').click()

driver.maximize_window()
time.sleep(5)
