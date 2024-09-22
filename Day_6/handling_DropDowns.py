import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
#Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()
dropdown_country_element = driver.find_element(By.XPATH, "//select[@id='input-country']")
time.sleep(5)
dropdown_country = select(dropdown_country_element)


#Select option from the dropdown
dropdown_country.select_by_visible_text("India")
dropdown_country.select_by_value("12")
dropdown_country.select_by_index("15")

#capture all the elements and print them
allOptions = dropdown_country.options
print("Total No..of Options available in the dropdown: ", len(allOptions))

for option in allOptions:
    print(option.text)