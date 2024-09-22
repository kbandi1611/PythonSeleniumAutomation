import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
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

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menu_admin_viewAdminModule']")))
driver.find_element(By.XPATH, "//span[normalize-space()='User Management']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Users']").click()
