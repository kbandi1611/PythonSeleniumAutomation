import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

# is_displayed() and is_enabled() methods
search_box = driver.find_element(By.XPATH, '//*[@id="small-searchterms"]')
print("Display Status: ", search_box.is_displayed())
print("Enabled Status: ", search_box.is_enabled())

# is_selected() method
male_radio_button = driver.find_element(By.XPATH, '//*[@id="gender-male"]')
female_radio_button = driver.find_element(By.XPATH, '//*[@id="gender-female"]')
print("Default radio button status:")
print(male_radio_button.is_selected())  # false
print(female_radio_button.is_selected())  # false

male_radio_button.click()
time.sleep(3)
print("After selecting male radio button: ")
print(male_radio_button.is_selected())  # True
print(female_radio_button.is_selected())  # False

female_radio_button.click()
time.sleep(3)
print("After selecting female radio button: ")
print(male_radio_button.is_selected())  # False
print(female_radio_button.is_selected())  # True
