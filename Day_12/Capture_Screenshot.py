import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(3)
# driver.save_screenshot("D:\\pythonProject\\PythonSelenium\\Day_12\\homepage.png")
driver.save_screenshot(os.getcwd()+"\\homepage.png")
# driver.get_screenshot_as_file(os.getcwd() + "\\homepage.png")
time.sleep(3)

################to save screenshot in binary format#######################
# driver.get_screenshot_as_base64()
# driver.get_screenshot_as_png()

driver.quit()
