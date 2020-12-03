from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    driver.find_element_by_id("book").click()
    button = driver.find_element_by_id("solve")
    driver.execute_script("arguments[0].scrollIntoView();", button)
    x_element = driver.find_element_by_id("input_value")
    x = x_element.text
    answer = calc(x)
    driver.find_element_by_id("answer").send_keys(answer)
    driver.find_element_by_id("solve").click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
    # не забываем оставить пустую строку в конце файла