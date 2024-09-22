from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)

driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.get("https://www.amazon.com/")

driver.back()
driver.forward()
driver.refresh()

driver.quit()
