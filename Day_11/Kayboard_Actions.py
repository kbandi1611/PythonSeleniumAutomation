# Ctrl + A
# Ctrl +C
# Tab
# Ctrl + V


import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://text-compare.com/")
driver.maximize_window()

input_box_1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
input_box_2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

input_box_1.send_keys("Welcome to Selenium")

act = ActionChains(driver)

# input_box_1 ----> Ctrl + A Select the text
# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
# input_box_1 ----> Ctrl + C    Copy the text
# act.key_down(Keys.CONTROL)
# act.send_keys("c")
# act.key_up(Keys.CONTROL)
# act.perform()
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# Press Tab key to navigate to second input box
# act.send_keys(Keys.TAB)
# act.perform()

act.send_keys(Keys.TAB).perform()

# input_box_2 ---> Ctrl + V Paste the text
# act.key_down(Keys.CONTROL)
# act.send_keys("v")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(5)
