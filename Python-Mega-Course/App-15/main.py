from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

prefs ={'download.default_directory' : os.getcwd()} # Current Working Directory
chrome_options.add_experimental_option('prefs',prefs)

service = Service("chromedriver-win64")
driver = webdriver.Chrome(options=chrome_options,service=service)
driver.get("https://demoqa.com/login")

#Login
username_field = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'userName')))
password_field = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'password')))
login_button = driver.find_element(By.ID,'login')

username_field.send_keys('name')
password_field.send_keys('pass')
driver.execute_script('arguments[0].click();',login_button)

#Navigate to form
elements = WebDriverWait(driver,
                         10).until(EC.visibility_of_element_located((By.XPATH,
                         '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
elements.click()
textbox = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'item-0')))
textbox.click()

#Capture Fields
fullname_field = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'userName')))
email_field = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'email')))
currenaddress_field = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'currenAddress')))
permanentaddress_field = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'permanentAddress')))
submit_button = driver.find_element(By.ID,'submit')

#Fill the fields
fullname_field.send_keys('name name')
email_field.send_keys('name@name.com')
currenaddress_field.send_keys('Australia')
permanentaddress_field.send_keys('New Zealand')
driver.execute_script('arguments[0].click();',submit_button)

#Download 
uplaod_download = (WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'item-7'))))
uplaod_download.click()
download_button = driver.find_element(By.ID,'downloadButton')
driver.execute_script('arguments[0].click();',download_button)

driver.quit()