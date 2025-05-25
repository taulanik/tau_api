import requests
import time
import json

# response = requests.get("https://playground.learnqa.ru/api/hello")
# print(response.text)
#
#
# print("Hello from Tau")


# json_text = {"messages": [{"message": "This is the first message", "timestamp": "2021-06-04 16:40:53"},
#                           {"message": "And this is a second message", "timestamp": "2021-06-04 16:41:01"}]}
#
# parsed_data = json_text
# second_message = parsed_data["messages"][1]
# print(second_message)

# response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
# redirect_count = len(response.history)
# final_url = response.url
# print(f"Количество редиректов: {redirect_count}")
# print(f"Конечный URL: {final_url}")

# url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
#
# # 1:Запрос без параметра method,
# response = requests.get(url)
# print(response.text)  # Запрос без параметра method возвращает 200, но выводит сообщение об ошибке, так как логика
# # сервера требует наличие params
# print(response.status_code)
# print()
#
# # 2: Запрос с неправильным методом (HEAD)
# response = requests.head(url)
# print(response.text)  # Запрос не из списка, не возвращает тело ответа, но можно увидеть статус код.
# print(response.status_code)
# print()
#
# # 3: Запрос с правильным методом (GET)
# response = requests.get(url, params={"params": "GET"})
# print(response.text)  # Запрос с правильным методом, возвращает сообщение о том что метод и параметр совпадают
# print(response.status_code)
# print()
#
# # 4: Проверка всех возможных комбинаций методов и параметров
# methods = ["GET", "POST", "PUT", "DELETE"]
# for method in methods:
#     for param in methods:
#         print(f"Проверка: метод {method}, параметр {param}")
#         if method == "GET":
#             response = requests.get(url, params={"method": param})
#         else:
#             response = requests.request(method, url, data={"method": param})
#         print(response.text)
#         print(response.status_code)
#         print()

# url = "https://playground.learnqa.ru/ajax/api/longtime_job"
#
# # Отправляем запрос без параметра token
# response_create_task = requests.get(url)
# print(response_create_task.text)
#
# # Извлекаем данные из ответа
# task_data = response_create_task.json()
# token = task_data["token"]
# seconds_to_wait = task_data["seconds"]
# print(f"Token: {token}, Время выполнения: {seconds_to_wait} секунд")
# print()
#
# # Отправляем запрос с token
# response_check_before = requests.get(url, params={"token": token})
# print(response_check_before.json())
# print()
#
# # Проверяем поле status
# status_before = response_check_before.json().get("status")
# assert status_before == "Job is NOT ready", f"Неверный статус: {status_before}"
# print("Статус корректен: Job is NOT ready")
# print()
#
# # Ожидаем завершения задачи
# print(f"Ожидание {seconds_to_wait} секунд...")
# time.sleep(seconds_to_wait)
# print("Ожидание завершено")
# print()
#
# # Проверка статуса задачи после завершения
# # Отправляем запрос с token
# response_check_after = requests.get(url, params={"token": token})
# print(response_check_after.json())
# print()
#
# # Проверяем поле status и result
# status_after = response_check_after.json().get("status")
# result_after = response_check_after.json().get("result")
# assert status_after == "Job is ready", f"Неверный статус: {status_after}"
# assert result_after is not None, "Поле result отсутствует"
# print(f"Статус корректен: Job is ready, Результат: {result_after}")

# Логин
login = "super_admin"

# Список паролей
passwords = [
    "password", "123456", "123456789", "12345678", "12345", "1234567", "1234567890",
    "qwerty", "abc123", "111111", "123123", "admin", "1234", "letmein", "welcome",
    "monkey", "password1", "sunshine", "master", "hello", "freedom", "whatever",
    "qazwsx", "trustno1", "dragon"
]

# Перебор паролей
for password in passwords:
    # Получаем авторизационную cookie
    response_password = requests.post(
        "https://playground.learnqa.ru/ajax/api/get_secret_password_homework",
        data={"login": login, "password": password}
    )

    # Извлекаем cookie
    cookie = response_password.cookies.get("auth_cookie")

    # Проверяем авторизацию с этой cookie
    if cookie:
        response_auth = requests.get(
            "https://playground.learnqa.ru/ajax/api/check_auth_cookie",
            cookies={"auth_cookie": cookie}
        )
        auth_message = response_auth.text

        # Если авторизация успешна, выводим результат
        if auth_message == "You are authorized":
            print(f"Найден правильный пароль: {password}")
            print(f"Сообщение: {auth_message}")
            break
    else:
        print(f"Cookie не получена для пароля: {password}")
