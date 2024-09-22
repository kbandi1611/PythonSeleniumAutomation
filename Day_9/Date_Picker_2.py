import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

#Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

#Date of birth
driver.find_element(By.XPATH, "//*[@id='dob']").click()

datepicker_month = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
datepicker_month.select_by_visible_text("Nov")
datepicker_year = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
datepicker_year.select_by_visible_text("1996")
all_dates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']/table/tbody/tr/td/a")

for date in all_dates:
    if date.text == "16":
        date.click()
        break
time.sleep(5)