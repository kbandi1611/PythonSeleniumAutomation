import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)    #switch_to_frame

#driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("06/08/1998")

year = "2025"
month = "march"
date = "20"

driver.find_element(By.XPATH, "//*[@id='datepicker']").click() #opens date picker

while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text.lower()
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text.lower()
    if month.lower() == mon and year == yr:
        break
    else:
        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[2]/span').click()  # Next arrow mark
        # driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[1]/span').click() #Previous arrow mark

dates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for DATE in dates:
    if DATE.text == date:
        DATE.click()
        break
time.sleep(5)
driver.quit()
