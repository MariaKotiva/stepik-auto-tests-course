from selenium import webdriver
import time

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/cats.html")
    driver.find_element_by_id("button")

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
    # не забываем оставить пустую строку в конце файла

