import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

act = ActionChains(driver)
act.context_click(button).perform()
time.sleep(5)
