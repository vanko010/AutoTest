import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import json
import xpath

def checkhovaten():
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    # Mở trình duyệt ở chế độ toàn màn hình
    driver.maximize_window()
    # Truy cập trang web
    driver.get("https://webdemo5.pavietnam.vn/2020_hctechco/lien-he")

    with open("datahovaten.json", "r", encoding='utf-8') as file_hovaten:
        dbhovaten = json.load(file_hovaten)
    hovaten = driver.find_element(By.XPATH, xpath.xhovaten)
    sdt = driver.find_element(By.XPATH, xpath.xsdt)
    email = driver.find_element(By.XPATH,xpath.xemail)
    diachi = driver.find_element(By.XPATH,xpath.xdiachi)
    tieude = driver.find_element(By.XPATH,xpath.xtieude)
    noidung = driver.find_element(By.XPATH,xpath.xnoidung)
    # mbv = driver.find_element(By.XPATH,xpath.xmbv)
    btngui = driver.find_element(By.XPATH,xpath.xgui)
    btnlamlai = driver.find_element(By.XPATH,xpath.xlamlai)
    counter = 1
    for data in dbhovaten:
            for key,value in data.items():
                ten = data["hovaten"]
                hovaten.send_keys(ten)
                sdt.send_keys("0987654321")
                email.send_keys("test@gmail.com")
                diachi.send_keys("344 Huynh Tan Phat, phường Bình Thuận, quận 7, TPHCM")
                tieude.send_keys("Test Liên hệ")
                noidung.send_keys("Test liên hệ")
                # mbv.send_keys("1231123")
                btngui.click()
                time.sleep(3)
                try:
                    alert = driver.switch_to.alert
                    if alert.text == "Họ và tên chưa hợp lệ, vui lòng nhập lại!":
                        print(f"Case {counter} Họ tên fail, nhập lại")
                    elif alert.text == "Yêu cầu của bạn đã được gửi!":
                        print(f"Case {counter} Yêu cầu đã được gửi")
                    elif alert.text == "Nhập mã bảo vệ chưa đúng!":
                        print(f"Case {counter} Yêu cầu chưa được gửi đi")
                    else:
                        print(f"Case {counter} Chưa nhập mã bảo vệ")
                    alert = Alert(driver)
                    alert.accept()
                except:
                    print(f"{counter}Case ngoại lệ, check lại")
                counter += 1
                hovaten.clear()
                sdt.clear()
                email.clear()
                diachi.clear()
                tieude.clear()
                noidung.clear()
                # mbv.clear()
    driver.close()
checkhovaten()

def checksdt():
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    # Mở trình duyệt ở chế độ toàn màn hình
    driver.maximize_window()
    # Truy cập trang web
    driver.get("https://webdemo5.pavietnam.vn/2020_hctechco/lien-he")
    hovaten = driver.find_element(By.XPATH, xpath.xhovaten)
    sdt = driver.find_element(By.XPATH, xpath.xsdt)
    email = driver.find_element(By.XPATH, xpath.xemail)
    diachi = driver.find_element(By.XPATH, xpath.xdiachi)
    tieude = driver.find_element(By.XPATH, xpath.xtieude)
    noidung = driver.find_element(By.XPATH, xpath.xnoidung)
    # mbv = driver.find_element(By.XPATH,xpath.xmbv)
    btngui = driver.find_element(By.XPATH, xpath.xgui)
    btnlamlai = driver.find_element(By.XPATH, xpath.xlamlai)
    with open("sdt.json", "r", encoding='utf-8') as file_sdt:
        dbsdt = json.load(file_sdt)
    counter = 1
    for key,value in dbsdt:
        vlsdt = dbsdt[value]
        hovaten.send_keys("Lê Đoàn Vũ")
        sdt.send_keys(vlsdt)
        email.send_keys("test@gmail.com")
        diachi.send_keys("344 Huynh Tan Phat, phường Bình Thuận, quận 7, TPHCM")
        tieude.send_keys("Test Liên hệ")
        noidung.send_keys("Test liên hệ")
        # mbv.send_keys("1231123")
        btngui.click()
        time.sleep(3)
        try:
            alert = driver.switch_to.alert
            if alert.text == "Họ và tên chưa hợp lệ, vui lòng nhập lại!":
                print(f"{counter}Họ tên fail, nhập lại")
            if alert.text == "Yêu cầu của bạn đã được gửi!":
                print(f"{counter}Yêu cầu đã được gửi")
            elif alert.text == "Nhập mã bảo vệ chưa đúng!":
                print(f"{counter}Yêu cầu chưa được gửi đi")
            else:
                print(f"{counter}Chưa nhập mã bảo vệ")
            alert = Alert(driver)
            alert.accept()
        except:
            print(f"{counter}Case ngoại lệ, check lại")
        counter += 1
        hovaten.clear()
        sdt.clear()
        email.clear()
        diachi.clear()
        tieude.clear()
        noidung.clear()
        # mbv.clear()