from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service=Service(executable_path='chromedriver.exe')
driver=webdriver.Chrome(service=service)

driver.get('https://youtube.com')

input=driver.find_element(By.XPATH, '//*[@id="search"]')
input.send_keys('google' + Keys.ENTER)
time.sleep(10)

driver.quit()