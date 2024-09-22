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

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
rome_element = driver.find_element(By.ID, "box6")
italy_element = driver.find_element(By.ID, "box106")
washington_element = driver.find_element(By.ID, "box3", )
untied_states_element = driver.find_element(By.ID, "box103")
oslo_element = driver.find_element(By.ID, "box1")
norway_element = driver.find_element(By.ID, "box101")
stockholm_element = driver.find_element(By.ID, "box2")
sweden_element = driver.find_element(By.ID, "box102")
copenhagen_element = driver.find_element(By.ID, "box4")
denmark_element = driver.find_element(By.ID, "box104")
seoul_element = driver.find_element(By.ID, "box5")
south_Korea_element = driver.find_element(By.ID, "box105")
madrid_element = driver.find_element(By.ID, "box7")
spain_element = driver.find_element(By.ID, "box107")

act = ActionChains(driver)
act.drag_and_drop(rome_element, italy_element).perform()
act.drag_and_drop(washington_element, untied_states_element).perform()
act.drag_and_drop(oslo_element, norway_element).perform()
act.drag_and_drop(stockholm_element, sweden_element).perform()
act.drag_and_drop(copenhagen_element, denmark_element).perform()
act.drag_and_drop(seoul_element, south_Korea_element).perform()
act.drag_and_drop(madrid_element, spain_element).perform()
time.sleep(5)

driver.quit()
