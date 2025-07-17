from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time
import csv

options = Options()
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

# Open and login
driver.get("https://assettiger.com/")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='menu-navbar']/div/a[2]")))
driver.find_element(By.XPATH, "//*[@id='menu-navbar']/div/a[2]").click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='LoginEmail']"))).send_keys("EMAIL")
driver.find_element(By.XPATH, "//*[@id='LoginPassword']").send_keys("PASSWORD")
driver.find_element(By.XPATH, "//*[@id='formLogin']/div/div[2]/div/div[4]/div/div/button[2]").click()
time.sleep(2)

# Navigate to checkout
driver.get("https://www.assettiger.com/checkout")
time.sleep(3)
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='formCheckOut']/div[1]/div[1]/a")))
driver.find_element(By.XPATH, "//*[@id='formCheckOut']/div[1]/div[1]/a").click()
time.sleep(1)

# Read all asset rows from CSV
with open('assets.csv', 'r') as file:
    reader = csv.DictReader(file)
    rows = list(reader)

# Use the first row to get person and site info
first_row = rows[0]
person_name = first_row['person_name'].strip()
person_email = first_row['person_email'].strip()
site = first_row['site'].strip()

# Loop through and add each asset
for row in rows:
    asset_code = row['asset_code'].strip()
    driver.find_element(By.ID, "query").send_keys(asset_code)
    driver.find_element(By.XPATH, "//*[@id='btn_query_search']").click()
    time.sleep(2)

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='All_assets']/tbody/tr/td[1]/label/span[1]"))
        ).click()
    except Exception as e:
        print(f"[!] Could not select asset {asset_code}: {e}")
        driver.find_element(By.ID, "query").clear()
        continue

    driver.find_element(By.ID, 'query').clear()

# Add to list
driver.find_element(By.XPATH, "//*[@id='addToListBtn']").click()
time.sleep(1)

# Select all pending items
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='pending_assets']/thead/tr/th[1]"))
)
driver.find_element(By.XPATH, "//*[@id='pending_assets']/thead/tr/th[1]").click()

# Select person
driver.find_element(By.XPATH, "//*[@id='select2-PersonId-container']").click()
person_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".select2-search__field"))
)
person_input.send_keys(person_name)
time.sleep(2)
person_input.send_keys(Keys.ENTER)
time.sleep(2)

# Select site
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "SiteId")))
site_select = Select(driver.find_element(By.ID, "SiteId"))
site_select.select_by_visible_text(site)

# Update email
email_field = driver.find_element(By.XPATH, "//*[@id='PersonEmail']")
email_field.clear()
email_field.send_keys(person_email)
driver.find_element(By.ID, "updateEmail").click()

# CAPTCHA pause
input("Please solve CAPTCHA in the browser, then press Enter here to continue...")

# Submit once for all assets
driver.find_element(By.ID, "SubmitBtn").click()
print("✅ Submitted all assets in bulk.")

time.sleep(10)
driver.quit()
