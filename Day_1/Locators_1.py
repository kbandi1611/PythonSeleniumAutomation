import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)

# Navigate to the Facebook login page
driver.get("https://www.walmart.com/")
driver.maximize_window()
#driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/span/header/nav/ul/li[2]/a/div/div[2]').click()
driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/span/header/nav/ul/li[2]/div/div/button').click()
element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/div/span/header/nav/ul/li[2]/div/div/button')))
# driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/span/header/form/div/input').send_keys("sunscreen")
# driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/span/header/form/div/button[2]/i').click()
time.sleep(5)
driver.quit()