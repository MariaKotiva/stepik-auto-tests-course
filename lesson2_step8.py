from selenium import webdriver
import time

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/file_input.html")


    input1 = driver.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_name("email")
    input3.send_keys("yvymobfo@yomail.info")
    button = driver.find_element_by_name("file")
    button.send_keys("/Users/m.kotova/downloads/setdryftugyihu.txt")
    button2 = driver.find_element_by_class_name("btn-primary")
    button2.click()

finally:
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    driver.quit()
    # не забываем оставить пустую строку в конце файла

