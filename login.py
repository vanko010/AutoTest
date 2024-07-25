import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import xpath
# Specify the path to chromedriver.exe
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
# Truy cập trang web
driver.get("https://webdemo5.pavietnam.vn/2020_hctechco/myadmin/index.php?module=login")
#load data tài khoản
import json

with open("dataTK.json", "r", encoding='utf-8') as f:
    db = json.load(f)
login_true = "Trang quản trị"
for data in db:

    for key, value in data.items():
        tk = data["user"]
        mk = data["password"]
        email = driver.find_element(By.XPATH, xpath.xuser)
        email.send_keys(tk)
        pw = driver.find_element(By.XPATH, xpath.xpw)
        pw.send_keys(mk)
        btnlogin = driver.find_element(By.XPATH, xpath.btnlogin)
        btnlogin.click()
        title = driver.title()
        try:
            if title == login_true:
                print("Case true")
            else:
                time.sleep(2)
                alert = Alert(driver)
                alert.accept()
        except Exception as e:
            print("Case fail")
time.sleep(3)
driver.close()
