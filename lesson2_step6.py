from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    driver = webdriver.Chrome()
    driver.get("http://SunInJuly.github.io/execute_script.html")

    x_element = driver.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    answer = calc(x)
    print(answer)
    driver.find_element_by_id("answer").send_keys(answer)
    driver.find_element_by_id("robotCheckbox").click()

    button = driver.find_element_by_tag_name("button")
    driver.execute_script("arguments[0].scrollIntoView();", button)
    driver.find_element_by_id("robotsRule").click()
    button.click()
    assert True

finally:
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    driver.quit()
    # не забываем оставить пустую строку в конце файла
