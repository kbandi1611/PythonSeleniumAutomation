from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)
driver.get("https://demo.nopcommerce.com/login")
driver.maximize_window()

emailbox = driver.find_element(By.XPATH, '//*[@id="Email"]')
emailbox.clear()
emailbox.send_keys("abc@gmail.com")
print("result of text:", emailbox.text)
print("result of get_attribute():", emailbox.get_attribute('value'))

login_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button')
print("result of text:", login_button.text)
print("result of get_attribute():", login_button.get_attribute('type'))
