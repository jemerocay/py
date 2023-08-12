
from dotenv import load_dotenv
import os
from pathlib import Path
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import datetime
import pandas as pd


load_dotenv()
options = Options()
# options.add_argument('--no-sandbox')
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')  # Last I checked this was necessary.
# prefs = {"credentials_enable_service": False,
#      "profile.password_manager_enabled": False}
# options.add_experimental_option("prefs", prefs)
webdriver = webdriver.Chrome('chromedriver.exe',options=options)


#getting the list
df = pd.read_excel('trackforce_users_template.xlsx')

print(df['Login'].tolist())

usernames = df['Login'].tolist()

# input ('whats up')

with webdriver as driver:
    wait = WebDriverWait(driver,30)
    driver.get('https://report.address.com')
    # wait.until(presence_of_element_located((By.CLASS_NAME, "form-control")))
    username = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="User Name"]')
    password = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Password"]')
    username.send_keys('username')
    password.send_keys('password')
    # password = driver.find_element(By.ID, 'password')
    driver.find_element(By.CLASS_NAME ,"btn").click()
    wait.until(presence_of_element_located((By.CSS_SELECTOR, 'a[data-original-title="Users"]')))
    driver.find_element(By.CSS_SELECTOR, 'a[data-original-title="Users"]').click()

    wait.until(presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="User Name"]')))
    import time
    username_search_box = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="User Name"]')
    for user in usernames:
        time.sleep(5)
        username_search_box.clear()
        username_search_box.send_keys(user)
        driver.find_element(By.CSS_SELECTOR,'a.ng2-smart-action ng2-smart-action-edit-edit').click()
        input('clicked')

    print(driver.get_cookies())
    input('press to end this')
    # wait.until(presence_of_element_located((By.CLASS_NAME, "card-img-top")))


    # print(results)
driver.quit()
