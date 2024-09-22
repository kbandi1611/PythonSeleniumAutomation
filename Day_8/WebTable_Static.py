from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# count no.of rows and columns in a table
noOfRows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))  # rows
noOfColumns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th"))  # columns
# print("Total no.of rows in a table: ", noOfRows)
# print("Total no.of columns in a table: ", noOfColumns)

# Read specific row and column data
# data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text #5th row and 1st column data
# print(data) # Master In Selenium

# Read all the rows and all the columns data

# for r in range(2, noOfRows+1):
#     for c in range(1, noOfColumns+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data, end = "   ")
#     print()

# Read the data based on condition(List books name whose author is Mukesh)
for r in range(2, noOfRows + 1):
    authorName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[2]").text
    print(authorName)
    if authorName == "Mukesh":
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(bookName, " written by ", authorName, " and its price is ", price)

driver.close()
