from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)

driver.get("https://whatmylocation.com/")
driver.maximize_window()
