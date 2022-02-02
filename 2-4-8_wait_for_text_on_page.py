# 2.4.8 Задание: ждем нужный текст на странице

# Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. 
# Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

#     Открыть страницу http://suninjuly.github.io/explicit_wait2.html
#     Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
#     Нажать на кнопку "Book"
#     Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element 
# из библиотеки expected_conditions.

# Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 15 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"),"$100")
        )

    # Нажимаем на кнопку "Book"
    browser.find_element_by_id("book").click()

    # Поиск заданного числа X
    x = browser.find_element_by_id("input_value").text
    # Решение математической задачи ln(abs(12*sin(x))) и запись ответа в поле ввода
    browser.find_element_by_id("answer").send_keys(str(math.log(abs(12*math.sin(int(x))))))
    # Нажатие на кнопку отправки ответа
    browser.find_element_by_id("solve").click()
finally:
    # Пауза для проверки ответа сервера
    time.sleep(60)
    # Если все правильно, будет сообщение, типа:
    # Congrats, you've passed the task! Copy this code as the answer to Stepik quiz: 29.006825990721875
    browser.quit()