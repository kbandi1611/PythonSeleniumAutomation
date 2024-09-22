from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()
outer_frame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer_frame)

inner_frame = driver.find_element(By.XPATH, '/html/body/section/div/div/iframe')
driver.switch_to.frame(inner_frame)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Welcome")

driver._switch_to.parent_frame()  # directly switch to parent frame(outer Iframe)
