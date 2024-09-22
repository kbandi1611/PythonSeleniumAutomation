import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# click on a link
# driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/ul[1]/li[4]/a").click()
# driver.find_element(By.LINK_TEXT, 'Digital downloads').click()
# driver.find_element(By.PARTIAL_LINK_TEXT, 'Digital').click()

# Find no.of links available in a page
links = driver.find_elements(By.TAG_NAME, 'a')
links = driver.find_elements(By.XPATH, '//a')
print(len(links))

# print all the links available in a web page
for link in links:
    print(link.text)

time.sleep(3)
