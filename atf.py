from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from PIL import Image
#from Screenshot import Screenshot_clipping

import time
#import csv

'''
Test Case No.1 
Checking out of Items
Expecting Results: To be able to checkout assets

Logging In : Successful
Navigating to Checkout assets: Successful
Adding multiple assets: Successful
'''

options = Options()
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()

driver.get("https://assettiger.com/")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='menu-navbar']/div/a[2]")) 
) 

login = driver.find_element(By.XPATH, "//*[@id='menu-navbar']/div/a[2]")
login.click() #finding the signin button


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='LoginEmail']"))).send_keys("EMAIL")
driver.find_element(By.XPATH, "//*[@id='LoginPassword']").send_keys("PASSWORD")
driver.find_element(By.XPATH, "//*[@id='formLogin']/div/div[2]/div/div[4]/div/div/button[2]").click()
time.sleep(2) #login the credentials

WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='nav-assets']/a"))) #//*[@id='nav-2-check-out']/a/span[2]
driver.find_element(By.XPATH, "//*[@id='nav-assets']/a").click()
WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='nav-2-check-out']")))
driver.find_element(By.XPATH, "//*[@id='nav-2-check-out']").click()
time.sleep(3) #navigating to the checkout, Another resolution for not clicking the href : driver.get("https://www.assettiger.com/checkout")

WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='formCheckOut']/div[1]/div[1]/a")))
driver.find_element(By.XPATH, "//*[@id='formCheckOut']/div[1]/div[1]/a").click()
time.sleep(1)
"""
with open('assets.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Read header row
    data = []
    for row in reader:
        data.append(row)
"""
"""
ITEM NO. 1
"""
driver.find_element(By.ID, "query").send_keys("TEST001")
driver.find_element(By.XPATH, "//*[@id='btn_query_search']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='All_assets']/tbody/tr/td[1]/label/span[1]").click() 
driver.find_element(By.ID, 'query').clear()

"""
ITEM NO. 2
"""
driver.find_element(By.ID, "query").send_keys("TEST002")
driver.find_element(By.XPATH, "//*[@id='btn_query_search']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='All_assets']/tbody/tr/td[1]/label/span[1]").click()
driver.find_element(By.ID, 'query').clear()

"""
ITEM NO. 3
"""

driver.find_element(By.ID, "query").send_keys("TEST003")
driver.find_element(By.XPATH, "//*[@id='btn_query_search']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='All_assets']/tbody/tr/td[1]/label/span[1]").click()

"""
Add item to the list
"""
driver.find_element(By.XPATH, "//*[@id='addToListBtn']").click()
time.sleep(1)
"""
Click the checkbox to add all the item
"""
WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='pending_assets']/thead/tr/th[1]")))
driver.find_element(By.XPATH, "//*[@id='pending_assets']/thead/tr/th[1]").click()

"""
Select site for employee
"""
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='SiteId']")))
site = driver.find_element(By.XPATH, "//*[@id='SiteId']")
site.click()

"""
Select the Vinson
"""
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='SiteId']/option[2]")))
site1 = driver.find_element(By.XPATH, "//*[@id='SiteId']/option[2]")
site1.click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='formCheckOut']/div[1]/div[5]/div[1]/div[3]/div/div/span/span[1]/span")))
driver.find_element(By.XPATH, "//*[@id='formCheckOut']/div[1]/div[5]/div[1]/div[3]/div/div/span/span[1]/span").click()
time.sleep(10)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "//*[@id='select2-PersonId-container']")))
driver.find_element(By.XPATH, "//*[@id='select2-PersonId-container'']").click()

WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "//*[@id='kt_body']/span/span/span[1]/input")))
driver.find_element(By.CLASS_NAME, "//*[@id='kt_body']/span/span/span[1]/input").send_keys("TEST MAN")


# Pause to let you solve CAPTCHA manually
input("Please solve the CAPTCHA manually in the browser, then press Enter here to continue...")



time.sleep(50) 
driver.quit()
