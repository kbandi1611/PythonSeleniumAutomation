import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# opens alert window
driver.find_element(By.XPATH, '//button[normalize-space()="Click for JS Prompt"]').click()
time.sleep(5)

alert_window = driver.switch_to.alert
print(alert_window.text)
alert_window.send_keys("Welcome")
alert_window.accept()  # close alert window by using OK button
# alert_window.dismiss() #close alert window by using cancel button
time.sleep(3)
