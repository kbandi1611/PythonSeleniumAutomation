import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

register_link = Keys.CONTROL + Keys.RETURN
driver.find_element(By.LINK_TEXT, "Register").send_keys(register_link)

# New Tab ---- Selenium 4 --- Opens a new tab and switch to new tab
driver.get("https://www.opencart.com")
time.sleep(2)
driver.switch_to.new_window("tab")
driver.get("https://www.openhrm.com")

# New Window ---- Selenium 4 --- Opens a new window and switch to new window
driver.get("https://www.opencart.com")
time.sleep(2)
driver.switch_to.new_window("window")
driver.get("https://www.openhrm.com")

time.sleep(3)
driver.quit()
