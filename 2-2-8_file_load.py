# Задание: загрузка файла

# В этом задании в форме регистрации требуется загрузить текстовый файл.

# Напишите скрипт, который будет выполнять следующий сценарий:

#     Открыть страницу http://suninjuly.github.io/file_input.html
#     Заполнить текстовые поля: имя, фамилия, email
#     Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
#     Нажать кнопку "Submit"

# Если все сделано правильно и быстро, вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

from selenium import webdriver
import os, time

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

browser.find_element_by_css_selector("[name=firstname]").send_keys("FirstName")
browser.find_element_by_css_selector("[name=lastname]").send_keys("LastName")
browser.find_element_by_css_selector("[name=email]").send_keys("first-last@email.dom")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt') 
# print(file_path)

browser.find_element_by_css_selector("[type=file]").send_keys(file_path)

browser.find_element_by_css_selector(".btn.btn-primary").click()
time.sleep(10)
browser.quit()

# Congrats, you've passed the task! Copy this code as the answer for Stepik quiz: 28.920111445053625
