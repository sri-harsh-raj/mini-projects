from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://youtube.com')

# Try locating the input element using CSS_SELECTOR
input = driver.find_element(By.CSS_SELECTOR, 'input#search')




driver.execute_script("arguments[0].setAttribute('value', 'google')", input)


# Send keys to the input element
input.send_keys('google' + Keys.ENTER)

time.sleep(10)

driver.quit()