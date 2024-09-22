# We need to install requests package through File --> Settings --> Project Interpreter --> Click on '+' symbol --> requests

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
all_links = driver.find_elements(By.TAG_NAME, "a")
print("Total links available on the page: ", len(all_links))
count = 0

for link in all_links:
    url = link.get_attribute("href")
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print(url, " is a broken link")
        count += 1
    else:
        print(url, " is a valid link")

print("Total no.of broken links: ", count)
