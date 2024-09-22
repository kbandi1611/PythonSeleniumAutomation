from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# capture cookies from the browser
cookies = driver.get_cookies()
print("No.of cookies:", len(cookies))  # 3

# Print details of all the cookies
for c in cookies:
    print(c)
    print(c.get("name"), ":", c.get('value'))

# Adding new cookie to the browser
driver.add_cookie({"name": "My_Cookie", "value": "12345"})
cookies = driver.get_cookies()
print("Size of cookies after adding new cookie:", len(cookies))

# Delete specific cookie from the browser
driver.delete_cookie("My_Cookie")
cookies = driver.get_cookies()
print("Size of cookies after deleting the new cookie:", len(cookies))

# Delete all the cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("Size of cookies after deleting all the cookie:", len(cookies))
