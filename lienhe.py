import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
# from webdriver_manager.chrome import ChromeDriverManager
import json
import xpath

def setup_driver():
    # #Code chạy linux
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

    #Code chạy window
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://webdemo5.pavietnam.vn/2020_hctechco/lien-he")
    return driver
def load_file(fileload):
    with open(fileload, "r", encoding='utf-8') as file_hovaten:
        return json.load(file_hovaten)
def fill_hovaten(driver, data):
    driver.find_element(By.XPATH, xpath.xhovaten).send_keys(data["hovaten"])
    driver.find_element(By.XPATH, xpath.xsdt).send_keys("0987654321")
    driver.find_element(By.XPATH, xpath.xemail).send_keys("test@gmail.com")
    driver.find_element(By.XPATH, xpath.xdiachi).send_keys("344 Huynh Tan Phat, phường Bình Thuận, quận 7, TPHCM")
    driver.find_element(By.XPATH, xpath.xtieude).send_keys("Test Liên hệ")
    driver.find_element(By.XPATH, xpath.xnoidung).send_keys("Test liên hệ")
    # driver.find_element(By.XPATH, xpath.xmbv).send_keys("1231123")
def submit_form(driver):
    driver.find_element(By.XPATH,xpath.xgui).click()
    # driver.find_element(By.XPATH,xpath.xlamlai).click()
def check_alert(driver,counter):
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
def clear_data(driver):
    driver.find_element(By.XPATH, xpath.xhovaten).clear()
    driver.find_element(By.XPATH, xpath.xsdt).clear()
    driver.find_element(By.XPATH, xpath.xemail).clear()
    driver.find_element(By.XPATH, xpath.xdiachi).clear()
    driver.find_element(By.XPATH, xpath.xtieude).clear()
    driver.find_element(By.XPATH, xpath.xnoidung).clear()
def checkhovaten():
    driver = setup_driver()
    dbhovaten = load_file ("datahovaten.json")
    counter = 1
    for data in dbhovaten:
                fill_hovaten(driver,data)
                submit_form(driver)
                time.sleep(1)
                check_alert(driver,counter)
                clear_data(driver)
                counter += 1

    driver.close()

def fill_sdt(driver,data):
    driver.find_element(By.XPATH, xpath.xhovaten).send_keys("Lê Đoàn Vũ")
    driver.find_element(By.XPATH, xpath.xsdt).send_keys(data["sodienthoai"])
    driver.find_element(By.XPATH, xpath.xemail).send_keys("test@gmail.com")
    driver.find_element(By.XPATH, xpath.xdiachi).send_keys("344 Huynh Tan Phat, phường Bình Thuận, quận 7, TPHCM")
    driver.find_element(By.XPATH, xpath.xtieude).send_keys("Test Liên hệ")
    driver.find_element(By.XPATH, xpath.xnoidung).send_keys("Test liên hệ")
    # driver.find_element(By.XPATH, xpath.xmbv).send_keys("1231123")
def checksdt():
    driver= setup_driver()
    dbsdt = load_file("dbsodienthoai.json")
    counter = 1
    for data in dbsdt:
        fill_sdt(driver,data)
        submit_form(driver)
        time.sleep(1)
        check_alert(driver,counter)
        clear_data(driver)
        counter +=1
    driver.close()

def fill_email(driver,data):
    driver.find_element(By.XPATH, xpath.xhovaten).send_keys("Lê Đoàn Vũ")
    driver.find_element(By.XPATH, xpath.xsdt).send_keys("0987654321")
    driver.find_element(By.XPATH, xpath.xemail).send_keys(data["email"])
    driver.find_element(By.XPATH, xpath.xdiachi).send_keys("344 Huynh Tan Phat, phường Bình Thuận, quận 7, TPHCM")
    driver.find_element(By.XPATH, xpath.xtieude).send_keys("Test Liên hệ")
    driver.find_element(By.XPATH, xpath.xnoidung).send_keys("Test liên hệ")
    # driver.find_element(By.XPATH, xpath.xmbv).send_keys("1231123")

def checkemail():
    driver = setup_driver()
    dbemail = load_file("dbemail.json")
    counter = 1
    for data in dbemail:
        fill_email(driver,data)
        submit_form(driver)
        time.sleep(1)
        check_alert(driver, counter)
        clear_data(driver)
        counter += 1
    driver.close()

def fill_diachi(driver, data):
    driver.find_element(By.XPATH, xpath.xhovaten).send_keys("Lê Đoàn Vũ")
    driver.find_element(By.XPATH, xpath.xsdt).send_keys("0987654321")
    driver.find_element(By.XPATH, xpath.xemail).send_keys("test@gmail.com")
    driver.find_element(By.XPATH, xpath.xdiachi).send_keys(data["diachi"])
    driver.find_element(By.XPATH, xpath.xtieude).send_keys("Test Liên hệ")
    driver.find_element(By.XPATH, xpath.xnoidung).send_keys("Test liên hệ")
    # driver.find_element(By.XPATH, xpath.xmbv).send_keys("1231123")

def checkdiachi():
    driver = setup_driver()
    dbdiachi = load_file("dbdiachi.json")
    counter = 1
    for data in dbdiachi:
        fill_diachi(driver,data)
        submit_form(driver)
        time.sleep(1)
        check_alert(driver,counter)
        clear_data(driver)
        counter += 1
    driver.close()

def fill_tieude(driver, data):
    driver.find_element(By.XPATH, xpath.xhovaten).send_keys("Lê Đoàn Vũ")
    driver.find_element(By.XPATH, xpath.xsdt).send_keys("0987654321")
    driver.find_element(By.XPATH, xpath.xemail).send_keys("test@gmail.com")
    driver.find_element(By.XPATH, xpath.xdiachi).send_keys("344 Huynh Tan Phat, phường Bình Thuận, quận 7, TPHCM")
    driver.find_element(By.XPATH, xpath.xtieude).send_keys(data["tieude"])
    driver.find_element(By.XPATH, xpath.xnoidung).send_keys("Test liên hệ")
    # driver.find_element(By.XPATH, xpath.xmbv).send_keys("1231123")

def checktieude():
    driver = setup_driver()
    dbtieude = load_file("dbtieude.json")
    counter = 1
    for data in dbtieude:
        fill_tieude(driver,data)
        submit_form(driver)
        time.sleep(1)
        check_alert(driver,counter)
        clear_data(driver)
        counter += 1
    driver.close()

def fill_noidung(driver, data):
    driver.find_element(By.XPATH, xpath.xhovaten).send_keys("Lê Đoàn Vũ")
    driver.find_element(By.XPATH, xpath.xsdt).send_keys("0987654321")
    driver.find_element(By.XPATH, xpath.xemail).send_keys("test@gmail.com")
    driver.find_element(By.XPATH, xpath.xdiachi).send_keys("344 Huynh Tan Phat, phường Bình Thuận, quận 7, TPHCM")
    driver.find_element(By.XPATH, xpath.xtieude).send_keys("Test liên hệ")
    driver.find_element(By.XPATH, xpath.xnoidung).send_keys(data["noidung"])
    # driver.find_element(By.XPATH, xpath.xmbv).send_keys("1231123")

def checknoidung():
    driver = setup_driver()
    dbnoidung = load_file("dbtieude.json")
    counter = 1
    for data in dbnoidung:
        fill_noidung(driver,data)
        submit_form(driver)
        time.sleep(1)
        check_alert(driver,counter)
        clear_data(driver)
        counter += 1
    driver.close()