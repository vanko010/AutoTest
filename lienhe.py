import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
# from webdriver_manager.chrome import ChromeDriverManager
import json
import xpath
import requests
from io import BytesIO
from PIL import Image
import pytesseract

def setup_driver():
    # Đường dẫn đến chromedriver
    chromedriver_path = '/usr/local/bin/chromedriver'

    # Khởi tạo đối tượng Service với đường dẫn đến chromedriver
    service = Service(chromedriver_path)

    # Tạo driver Chrome với service đã khởi tạo
    driver = webdriver.Chrome(service=service)

    # Mở rộng cửa sổ trình duyệt
    driver.maximize_window()
    driver.get("https://webdemo5.pavietnam.vn/2020_hctechco/lien-he")
    return driver
def load_file(fileload):
    with open(fileload, "r", encoding='utf-8') as file_hovaten:
        return json.load(file_hovaten)

def get_captcha_text(driver):
    captcha_element = driver.find_element(By.XPATH, xpath.xcaptcha)
    captcha_image_url = captcha_element.get_attribute('src')
    response = requests.get(captcha_image_url)
    img = Image.open(BytesIO(response.content))
    # Sử dụng OCR để nhận diện captcha
    captcha_text = pytesseract.image_to_string(img)
    return captcha_text.strip()

def fill_data(driver, data, captcha_text=None):
    driver.find_element(By.XPATH, xpath.xhovaten).send_keys(data["hovaten"])
    driver.find_element(By.XPATH, xpath.xsdt).send_keys(data["sodienthoai"])
    driver.find_element(By.XPATH, xpath.xemail).send_keys(data["email"])
    driver.find_element(By.XPATH, xpath.xdiachi).send_keys(data["diachi"])
    driver.find_element(By.XPATH, xpath.xtieude).send_keys(data["tieude"])
    driver.find_element(By.XPATH, xpath.xnoidung).send_keys(data["noidung"])
    if captcha_text:
        driver.find_element(By.XPATH, xpath.xmbv).send_keys(captcha_text)
def submit_form(driver):
    driver.find_element(By.XPATH,xpath.xgui).click()
    # driver.find_element(By.XPATH,xpath.xlamlai).click()
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
        captcha_text = get_captcha_text(driver)
        fill_data(driver, data)
        submit_form(driver)
        # time.sleep(1)

        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.accept()

            if counter == 4 or counter == 6:
                print(f"Case {counter} check fail")
                if alert_text == "Họ và tên chưa hợp lệ, vui lòng nhập lại!":
                    print(f"Case {counter} -> Pass")
                else:
                    print(f"Case {counter} -> Fail")
            else:
                print(f"Case {counter} check true")
                if alert_text == "Yêu cầu của bạn đã được gửi!":
                    print(f"Case {counter} -> Pass")
                elif alert_text == "Vui lòng nhập mã bảo vệ!":
                    print(f"Case {counter} Chưa nhập mã bảo vệ")
                else:
                    print(f"Case {counter} -> Fail")

        except:
            try:
                alert = driver.switch_to.alert
                if alert.text == "Nhập mã bảo vệ chưa đúng!":
                    print(f"{counter} mã bảo vệ sai")
                else:
                    print(f"Case {counter} ngoại lệ -> Check lại")
                alert.accept()
            except:
                print(f"Case {counter} ngoại lệ -> Không có alert")

        clear_data(driver)
        counter += 1

    driver.close()

def checksdt():
    driver= setup_driver()
    dbsdt = load_file("dbsodienthoai.json")
    counter = 1
    for data in dbsdt:
        fill_data(driver,data)
        submit_form(driver)
        # time.sleep(1)
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            if counter == 1 or counter == 5:
                print(f"Case {counter} check true")
                if alert_text == "Yêu cầu của bạn đã được gửi!":
                    print(f"Case {counter} -> Pass")
                else:
                    if alert_text == "Vui lòng nhập mã bảo vệ!":
                        print("Chưa nhập mã bảo vệ")
                    elif alert.text == "Nhập mã bảo vệ chưa đúng!":
                        print("Mã bảo vệ chưa đúng")
                    else:
                        print(f"Case {counter} -> Fail")
            else:
                print(f"Case {counter} check fail")
                if alert_text == "Số điện thoại không hợp lệ!":
                    print(f"Case {counter} -> Pass")
                else:
                    if alert_text == "Vui lòng nhập mã bảo vệ!":
                        print("Chưa nhập mã bảo vệ")
                    elif alert.text == "Nhập mã bảo vệ chưa đúng!":
                        print("Mã bảo vệ chưa đúng")
                    else:
                        print(f"Case {counter} -> Fail")

        except:
            try:
                alert = driver.switch_to.alert
                if alert.text == "Nhập mã bảo vệ chưa đúng!":
                    print(f"{counter} mã bảo vệ sai")
                else:
                    print(f"Case {counter} ngoại lệ -> Check lại")
                alert.accept()
            except:
                print(f"Case {counter} ngoại lệ -> Không có alert")

        clear_data(driver)
        counter += 1
    driver.close()

def checkemail():
    driver = setup_driver()
    dbemail = load_file("dbemail.json")
    counter = 1
    for data in dbemail:
        fill_data(driver, data)
        submit_form(driver)
        # time.sleep(1)
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            if counter == 7 or counter == 8 or counter == 9:
                print(f"Case {counter} check fail")
                if alert_text == "Email không hợp lệ!":
                    print(f"Case {counter} -> Pass")
                else:
                    if alert_text == "Vui lòng nhập mã bảo vệ!":
                        print("Chưa nhập mã bảo vệ")
                    elif alert.text == "Nhập mã bảo vệ chưa đúng!":
                        print("Mã bảo vệ chưa đúng")
                    else:
                        print(f"Case {counter} -> Fail")
            else:
                print(f"Case {counter} check true")
                if alert_text == "Yêu cầu của bạn đã được gửi!":
                    print(f"Case {counter} -> Pass")
                else:
                    if alert_text == "Vui lòng nhập mã bảo vệ!":
                        print("Chưa nhập mã bảo vệ")
                    elif alert.text == "Nhập mã bảo vệ chưa đúng!":
                        print("Mã bảo vệ chưa đúng")
                    else:
                        print(f"Case {counter} -> Fail")

        except:
            try:
                alert = driver.switch_to.alert
                if alert.text == "Nhập mã bảo vệ chưa đúng!":
                    print(f"{counter} mã bảo vệ sai")
                else:
                    print(f"Case {counter} ngoại lệ -> Check lại")
                alert.accept()
            except:
                print(f"Case {counter} ngoại lệ -> Không có alert")

        clear_data(driver)
        counter += 1
    driver.close()

def checkdiachi():
    driver = setup_driver()
    dbdiachi = load_file("dbdiachi.json")
    counter = 1
    for data in dbdiachi:
        fill_data(driver, data)
        submit_form(driver)
        # time.sleep(1)
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            if counter >=3 or counter <= 5:
                print(f"Case {counter} check fail")
                if alert_text == "Địa chỉ không hợp lệ!":
                    print(f"Case {counter} -> Pass")
                else:
                    if alert_text == "Vui lòng nhập mã bảo vệ!":
                        print("Chưa nhập mã bảo vệ")
                    elif alert.text == "Nhập mã bảo vệ chưa đúng!":
                        print("Mã bảo vệ chưa đúng")
                    else:
                        print(f"Case {counter} -> Fail")
            else:
                print(f"Case {counter} check true")
                if alert_text == "Yêu cầu của bạn đã được gửi!":
                    print(f"Case {counter} -> Pass")
                else:
                    if alert_text == "Vui lòng nhập mã bảo vệ!":
                        print("Chưa nhập mã bảo vệ")
                    elif alert.text == "Nhập mã bảo vệ chưa đúng!":
                        print("Mã bảo vệ chưa đúng")
                    else:
                        print(f"Case {counter} -> Fail")

        except:
            try:
                alert = driver.switch_to.alert
                if alert.text == "Nhập mã bảo vệ chưa đúng!":
                    print(f"{counter} mã bảo vệ sai")
                else:
                    print(f"Case {counter} ngoại lệ -> Check lại")
                alert.accept()
            except:
                print(f"Case {counter} ngoại lệ -> Không có alert")

        clear_data(driver)
        counter += 1
    driver.close()
def checktieude():
    driver = setup_driver()
    dbtieude = load_file("dbtieude.json")
    counter = 1
    for data in dbtieude:
        fill_data(driver, data)
        submit_form(driver)
        # time.sleep(1)
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            if counter >= 5:
                print(f"Case {counter} check fail")
                if alert_text == "Tiêu đề không hợp lệ!":
                    print(f"Case {counter} -> Pass")
                else:
                    if alert_text == "Vui lòng nhập mã bảo vệ!":
                        print("Chưa nhập mã bảo vệ")
                    elif alert.text == "Nhập mã bảo vệ chưa đúng!":
                        print("Mã bảo vệ chưa đúng")
                    else:
                        print(f"Case {counter} -> Fail")
            else:
                print(f"Case {counter} check true")
                if alert_text == "Yêu cầu của bạn đã được gửi!":
                    print(f"Case {counter} -> Pass")
                else:
                    if alert_text == "Vui lòng nhập mã bảo vệ!":
                        print("Chưa nhập mã bảo vệ")
                    elif alert.text == "Nhập mã bảo vệ chưa đúng!":
                        print("Mã bảo vệ chưa đúng")
                    else:
                        print(f"Case {counter} -> Fail")

        except:
            try:
                alert = driver.switch_to.alert
                if alert.text == "Nhập mã bảo vệ chưa đúng!":
                    print(f"{counter} mã bảo vệ sai")
                else:
                    print(f"Case {counter} ngoại lệ -> Check lại")
                alert.accept()
            except:
                print(f"Case {counter} ngoại lệ -> Không có alert")

        clear_data(driver)
        counter += 1
    driver.close()

def checknoidung():
    driver = setup_driver()
    dbnoidung = load_file("dbtieude.json")
    counter = 1
    for data in dbnoidung:
        fill_data(driver, data)
        submit_form(driver)
        # time.sleep(1)
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            if counter >= 5:
                print(f"Case {counter} check fail")
                if alert_text == "Nội dung không hợp lệ!":
                    print(f"Case {counter} -> Pass")
                else:
                    if alert_text == "Vui lòng nhập mã bảo vệ!":
                        print("Chưa nhập mã bảo vệ")
                    elif alert.text == "Nhập mã bảo vệ chưa đúng!":
                        print("Mã bảo vệ chưa đúng")
                    else:
                        print(f"Case {counter} -> Fail")
            else:
                print(f"Case {counter} check true")
                if alert_text == "Yêu cầu của bạn đã được gửi!":
                    print(f"Case {counter} -> Pass")
                else:
                    if alert_text == "Vui lòng nhập mã bảo vệ!":
                        print("Chưa nhập mã bảo vệ")
                    elif alert.text == "Nhập mã bảo vệ chưa đúng!":
                        print("Mã bảo vệ chưa đúng")
                    else:
                        print(f"Case {counter} -> Fail")

        except:
            try:
                alert = driver.switch_to.alert
                if alert.text == "Nhập mã bảo vệ chưa đúng!":
                    print(f"{counter} mã bảo vệ sai")
                else:
                    print(f"Case {counter} ngoại lệ -> Check lại")
                alert.accept()
            except:
                print(f"Case {counter} ngoại lệ -> Không có alert")

        clear_data(driver)
        counter += 1
    driver.close()