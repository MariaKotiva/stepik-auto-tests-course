from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/redirect_accept.html")

    button = driver.find_element_by_class_name("btn-primary")
    button.click()
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    x_element = driver.find_element_by_id("input_value")
    x = x_element.text
    answer = calc(x)
    driver.find_element_by_id("answer").send_keys(answer)
    driver.find_element_by_class_name("btn-primary").click()

finally:
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    driver.quit()
    # не забываем оставить пустую строку в конце файла

