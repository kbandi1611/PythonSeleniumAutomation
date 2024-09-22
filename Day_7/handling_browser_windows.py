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

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
window_id = driver.current_window_handle
print(window_id) #BD65C02204A1044FD2167F527E19F694, 41BCF0C3CFC3EC2DACCA078964C782D6 (executed 2 times so got 2 different window ID's)
time.sleep(5)
driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()
window_ids = driver.window_handles
print(window_ids)

#Approach 1
# parent_window_id = window_ids[0]
# child_window_id = window_ids[1]
# print(parent_window_id, child_window_id)
#
# driver.switch_to.window(child_window_id)
# time.sleep(5)
#
# print("Title of the child window", driver.title)
#
# driver.switch_to.window(parent_window_id)
# print("Title of the parent window", driver.title)
#
# time.sleep(5)

#Approach 2
# for win_id in window_ids:
#     driver.switch_to.window(win_id)
#     print(driver.title)

#close parent browser window
# for win_id in window_ids:
#     driver.switch_to.window(win_id)
#     if driver.title == "OrangeHRM":
#         driver.close()

#close child browser window
for win_id in window_ids:
    driver.switch_to.window(win_id)
    if driver.title == "Human Resources Management Software | OrangeHRM":
        time.sleep(3)
        driver.close()