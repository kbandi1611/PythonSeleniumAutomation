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
# driver.implicitly_wait(10)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
min_slider = driver.find_element(By.XPATH, "//span[1]")
max_slider = driver.find_element(By.XPATH, "//span[2]")

print("......................Locations of both sliders before moving....................")
print(min_slider.location)  # {'x': 59, 'y': 250}
print(max_slider.location)  # {'x': 612, 'y': 250}

act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider, 80, 0).perform()
act.drag_and_drop_by_offset(max_slider, -112, 0).perform()

print("......................Locations of both sliders after moving....................")
print(min_slider.location)  # {'x': 142, 'y': 250}
print(max_slider.location)  # {'x': 502, 'y': 250}

time.sleep(5)

driver.quit()
