import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os

# Get the current working directory
location = os.getcwd()
print(f"Download location: {location}")

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options

    # Set up ChromeOptions
    options = Options()

    # Set preferences for ChromeOptions
    preferences = {
        "download.default_directory": location,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", preferences)

    # Initialize the Chrome WebDriver with the service and options
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

driver = chrome_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download")
driver.maximize_window()

# Wait until the element is present
wait = WebDriverWait(driver, 10)
download_link = wait.until(EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[5]/a[1]")))

# Scroll to the element
driver.execute_script("arguments[0].scrollIntoView(true);", download_link)

# Click on the download link using JavaScript
driver.execute_script("arguments[0].click();", download_link)

# Adding a delay to ensure the file is downloaded
time.sleep(10)

# Close the driver
driver.quit()

# Verify the file is downloaded
downloaded_files = os.listdir(location)
print(f"Files in download location: {downloaded_files}")
