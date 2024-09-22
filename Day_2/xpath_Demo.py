import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)
driver.get("https://www.flipkart.com/")
driver.maximize_window()

# Absolute XPATH:
# driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input").send_keys("T-shirts")
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[2]/form[1]/div[1]/button[1]/*[name()='svg'][1]").click()

# Relative XPATH:
# driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input').send_keys("T-shirts")
# driver.find_element(By.XPATH, "//button[@title='Search for Products, Brands and More']//*[name()='svg']").click()

##############Getting Error for the below lines of code#########################
# OR operator:
# driver.find_element(By.XPATH, "//input[@name='q' or @type='text']").send_keys("T-shirts")
# driver.find_element(By.XPATH, )

# contains() & start-with methods:
# driver.find_element(By.XPATH, "//input[contains(@name, 'q')]").send_keys("T-shirts")
# # driver.find_element(By.XPATH, "//svg[start-with(@height=24)]").click()
# driver.find_element(By.XPATH, "//svg[starts-with(@height, '24')]").click()
# driver.find_element(By.XPATH, "//svg[starts-with(@height, '24')]").click()
#
# time.sleep(3)
