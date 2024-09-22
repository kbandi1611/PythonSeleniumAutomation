
import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
#Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(5)

driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='User Management']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Users']").click()


# time.sleep(5)


