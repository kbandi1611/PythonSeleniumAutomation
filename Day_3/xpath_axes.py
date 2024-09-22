from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeOptions to set the service
options = webdriver.ChromeOptions()
options.service = ChromeDriverManager().install()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

# self_node

# text_msg = driver.find_element(By.XPATH,'//*[@id="leftcontainer"]/table/tbody/tr[15]/td[1]/a/self::a').text
# print(text_msg)

# parent_node

# text_msg = driver.find_element(By.XPATH,'//*[@id="leftcontainer"]/table/tbody/tr[15]/td[1]/a/parent::td').text
# print(text_msg)

# child_node
# child = driver.find_elements(By.XPATH,'//*[@id="leftcontainer"]/table/tbody/tr[15]/td[1]/a/ancestor::tr/child::td')
# print(len(child))

# ancestor_node
# text_msg = driver.find_element(By.XPATH,'//*[@id="leftcontainer"]/table/tbody/tr[15]/td[1]/a/ancestor::tr').text
# print(text_msg)

# descendant node
# descendants = driver.find_elements(By.XPATH,'//*[@id="leftcontainer"]/table/tbody/tr[15]/td[1]/a/ancestor::tr/descendant::*')
# print("No.of descendants node:", len(descendants))

# following nodes
# following = driver.find_elements(By.XPATH,'//*[@id="leftcontainer"]/table/tbody/tr[15]/td[1]/a/ancestor::tr/following::*')
# print("No.of descendants node:", len(following))

# following sibling nodes
# following_siblings = driver.find_elements(By.XPATH,'//*[@id="leftcontainer"]/table/tbody/tr[15]/td[1]/a/ancestor::tr/following-sibling::*')
# print("No.of descendants node:", len(following_siblings))

# preceding nodes
# preceding = driver.find_elements(By.XPATH,'//*[@id="leftcontainer"]/table/tbody/tr[15]/td[1]/a/ancestor::tr/preceding::*')
# print(len(preceding))

# preceding sibling nodes
# preceding_siblings = driver.find_elements(By.XPATH,'//*[@id="leftcontainer"]/table/tbody/tr[15]/td[1]/a/ancestor::tr/preceding::tr')
# print(len(preceding_siblings))
