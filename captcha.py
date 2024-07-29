from PIL import Image
import pytesseract
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

def setup_driver():
    # Code chạy windows
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://webdemo5.pavietnam.vn/2020_hctechco/lien-he")
    return driver

def wait_for_element(driver, xpath, timeout=10):
    """Chờ cho phần tử xuất hiện trên trang"""
    end_time = time.time() + timeout
    while time.time() < end_time:
        try:
            element = driver.find_element(By.XPATH, xpath)
            if element.is_displayed():
                return element
        except:
            pass
        time.sleep(1)
    raise Exception(f"Element with xpath {xpath} not found")

def giai_captcha(driver, xpath):
    captcha_element = wait_for_element(driver, xpath)
    captcha_image = captcha_element.screenshot_as_png
    temp_image_path = 'captcha_temp.png'

    # Lưu ảnh captcha tạm thời
    with open(temp_image_path, 'wb') as file:
        file.write(captcha_image)

    # Mở và xử lý ảnh
    with Image.open(temp_image_path) as anh:
        anh = anh.convert('L')  # Chuyển đổi ảnh thành ảnh đen trắng
        anh = anh.point(lambda x: 0 if x < 140 else 255)  # Chuyển đổi ngưỡng

        # Sử dụng pytesseract để nhận diện văn bản từ ảnh
        van_ban_captcha = pytesseract.image_to_string(anh, config='--psm 8')  # Sử dụng mode nhận diện ký tự đơn

    os.remove(temp_image_path)  # Xóa ảnh tạm thời

    # Lọc và trả về văn bản captcha
    van_ban_captcha = ''.join(filter(str.isalnum, van_ban_captcha))
    return van_ban_captcha

# Ví dụ sử dụng:
driver = setup_driver()
van_ban_captcha = giai_captcha(driver, "//img[@id='img_contact_cap']")
print(f'Văn bản CAPTCHA: {van_ban_captcha}')

# Không đóng cửa sổ trình duyệt
driver.close()  # Không cần phải gọi driver.close() ở đây
driver.quit()   # Không cần phải gọi driver.quit() ở đây
