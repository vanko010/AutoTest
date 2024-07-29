import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager

import xpath
import json

def login():
    # Code chạy linux
    # driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    
    #Code chạy window
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver.get("https://webdemo5.pavietnam.vn/2020_hctechco/myadmin/index.php?module=login")
    #load data tài khoản
    with open("dataTK.json", "r", encoding='utf-8') as f:
        db = json.load(f)
    login_true = "Trang quản trị"
    counter = 1
    for data in db:
            tk = data["user"]
            mk = data["password"]
            email = driver.find_element(By.XPATH, xpath.xuser)
            email.clear()
            email.send_keys(tk)
            pw = driver.find_element(By.XPATH, xpath.xpw)
            pw.clear()
            pw.send_keys(mk)
            btnlogin = driver.find_element(By.XPATH, xpath.btnlogin)
            btnlogin.click()
            try:
                title = driver.title
                if title == login_true:
                    if counter == 18:
                         print(f"Case {counter} true -> Passed")
                    else:
                        print (f"Case {counter} là bug -> Check lại")
                    break
                else:
                    time.sleep(1)
                    alert = Alert(driver)
                    alert.accept()
            except Exception as e:
                if counter != 18:
                    print(f"Case {counter} check login fail")
                    print("-> Passed")
                else:
                    print(f"Case {counter} là bug -> Check lại")
                    print("-> Fail")
            counter += 1
    time.sleep(3)
    driver.close()
