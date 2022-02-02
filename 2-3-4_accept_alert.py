# Задание: принимаем alert

# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

#     Открыть страницу http://suninjuly.github.io/alert_accept.html
#     Нажать на кнопку
#     Принять confirm
#     На новой странице решить капчу для роботов, чтобы получить число с ответом

# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), 
# вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.

from selenium import webdriver
import time, math

try:
    browser = webdriver.Chrome()

    # Открываем страницу
    browser.get("http://suninjuly.github.io/alert_accept.html")
    
    # Нажимаем кнопку
    browser.find_element_by_css_selector(".btn.btn-primary").click()
    
    # Переключаемся на появившийся алерт и нажимаем подтверждение
    alert = browser.switch_to.alert
    alert.accept()

    # Решение математической задачи ln(abs(12*sin(x))) и запись ответа в поле ввода
    x = browser.find_element_by_id("input_value").text
    browser.find_element_by_id("answer").send_keys(str(math.log(abs(12*math.sin(int(x))))))
    browser.find_element_by_class_name("btn").click()
finally:
    # Пауза для проверки ответа сервера
    time.sleep(10)

    # Если все правильно, будет сообщение, типа:    
    # Congrats, you've passed the task! Copy this code as the answer to Stepik quiz: 28.962673067028827
    browser.quit()
