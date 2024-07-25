import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import xpath
# Specify the path to chromedriver.exe
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
# Truy cập trang web
driver.get("https://webdemo5.pavietnam.vn/2020_hctechco/myadmin/index.php?module=login")
try:
    email= driver.find_element(By.XPATH,xpath.xuser)
    email.send_keys("hctechco")
    pw = driver.find_element(By.XPATH,xpath.xpw)
    pw.send_keys("hctechco123!")
    btnlogin = driver.find_element(By.XPATH,xpath.btnlogin)
    btnlogin.click()
except Exception as e:
    print("Login fail")
time.sleep(3)
driver.close()
