import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)
# driver.implicitly_wait(10)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
time.sleep(5)

# 1. Scroll down page by pixel size
# driver.execute_script("window.scrollBy(0,3000)")
# value = driver.execute_script("return window.pageYOffset;")
# print("No.of pixels moved:", value)

# 2. Scroll down the page till the element is visible
# flag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();", flag)
# value = driver.execute_script("return window.pageYOffset;")
# print("No.of pixels moved:", value)

# 3. Scroll down page till end
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# value = driver.execute_script("return window.pageYOffset;")
# print("No.of pixels moved:", value)

# 4. Scroll upto starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("No.of pixels moved:", value)
time.sleep(3)
