from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time
#Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)
myWait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions= [NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, Exception])

driver.get("https://www.google.com")
driver.maximize_window()
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys("Selenium")
search_box.submit()

search_link = myWait.until(EC.presence_of_element_located((By.XPATH, '//h3[text()="Selenium"]')))
search_link.click()
