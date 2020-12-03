from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

def calc(x, y):
    return x + y

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/selects1.html")

    x_element = driver.find_element_by_id("num1")
    x1 = x_element.text
    x = int(x1)
    y_element = driver.find_element_by_id("num2")
    y1 = y_element.text
    y = int(y1)
    xy1 = calc(x, y)
    xy = str(xy1)
    driver.find_element_by_id("dropdown").click()
    select = Select(driver.find_element_by_id("dropdown"))
    select.select_by_value(xy)
    driver.find_element_by_xpath("/html/body/div/form/button").click()



finally:
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    driver.quit()
    # не забываем оставить пустую строку в конце файла

