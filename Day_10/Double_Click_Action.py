import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
driver.switch_to.frame('iframeResult')
field1 = driver.find_element(By.XPATH, '//*[@id="field1"]')
field1.clear()
field1 .send_keys("Welcome")
button = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")

act = ActionChains(driver)
act.double_click(button).perform()

time.sleep(5)