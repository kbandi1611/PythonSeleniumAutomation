import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)

driver.get("https://www.facebook.com/")
driver.maximize_window()

# tag & ID CSS Selector
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("bandikarthikkumarreddy@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("bandikarthikkumarreddy@gmail.com")

# tag & class CSS Selector
# driver.find_element(By.CSS_SELECTOR, 'input.inputtext').send_keys("bandikarthikkumarreddy@gmail.com")
# driver.find_element(By.CSS_SELECTOR, '.inputtext').send_keys("bandikarthikkumarreddy@gmail.com")

# tag & attribute CSS Selector
# driver.find_element(By.CSS_SELECTOR, 'input[data-testid=royal_email]').send_keys("bandikarthikkumarreddy@gmail.com")
driver.find_element(By.CSS_SELECTOR, '[data-testid=royal_email]').send_keys("bandikarthikkumarreddy@gmail.com")
driver.find_element(By.CSS_SELECTOR, '[data-testid=royal_pass]').send_keys('Karthik@123')
driver.find_element(By.CSS_SELECTOR, '[data-testid=royal_login_button]').click()

# tag, class & attribute CSS Selector
# driver.find_element(By.CSS_SELECTOR, 'input[data-testid=royal_pass]').send_keys("bandikarthikkumarreddy@gmail.com")

time.sleep(10)
