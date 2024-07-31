from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import time


def capture_captcha(driver_url, captcha_id, screenshot_path='screenshot.png', captcha_image_path='captcha.png'):
    # Khởi động trình duyệt
    driver = webdriver.Chrome()

    # Truy cập trang web chứa captcha
    driver.get(driver_url)
    driver.maximize_window()
    # Chờ cho phần tử captcha xuất hiện
    wait = WebDriverWait(driver, 10)
    captcha_element = wait.until(EC.presence_of_element_located((By.ID, captcha_id)))

    # Lấy vị trí và kích thước của captcha
    location = captcha_element.location
    size = captcha_element.size

    # Chụp màn hình toàn bộ trang
    driver.save_screenshot(screenshot_path)

    # Mở ảnh chụp màn hình và cắt phần captcha
    x = location['x']
    y = location['y']
    width = size['width']
    height = size['height']
    im = Image.open(screenshot_path)
    im = im.crop((x, y, x + width, y + height))
    im.save(captcha_image_path)

    # Hiển thị ảnh captcha (tuỳ chọn)
    im.show()

    # Chờ một thời gian để xem ảnh (tuỳ chọn)
    time.sleep(10)


# Sử dụng hàm
capture_captcha("https://webdemo5.pavietnam.vn/2020_hctechco/lien-he", 'img_contact_cap')
