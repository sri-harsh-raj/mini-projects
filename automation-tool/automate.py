from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
'''service = Service(executable_path='chromedriver.exe')'''
driver = webdriver.Chrome()
driver.get('https://web.careerwill.com/login')
driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-login > div > div > div > section.right.w-full.items-start > div.bg-white.p-10.rounded-3xl.shadow-lg.w-\[70\%\] > form > div:nth-child(1) > input').send_keys('9142172616')
driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-login > div > div > div > section.right.w-full.items-start > div.bg-white.p-10.rounded-3xl.shadow-lg.w-\[70\%\] > form > div:nth-child(2) > input').send_keys('education91')
driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-login > div > div > div > section.right.w-full.items-start > div.bg-white.p-10.rounded-3xl.shadow-lg.w-\[70\%\] > form > div.block > button').click()
time.sleep(10)
driver.quit()