import requests
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

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

# 1:Запрос без параметра method,
response = requests.get(url)
print(response.text)  # Запрос без параметра method возвращает 200, но выводит сообщение об ошибке, так как логика
# сервера требует наличие params
print(response.status_code)
print()

# 2: Запрос с неправильным методом (HEAD)
response = requests.head(url)
print(response.text)  # Запрос не из списка, не возвращает тело ответа, но можно увидеть статус код.
print(response.status_code)
print()

# 3: Запрос с правильным методом (GET)
response = requests.get(url, params={"params": "GET"})
print(response.text)  # Запрос с правильным методом, возвращает сообщение о том что метод и параметр совпадают
print(response.status_code)
print()

# 4: Проверка всех возможных комбинаций методов и параметров
methods = ["GET", "POST", "PUT", "DELETE"]
for method in methods:
    for param in methods:
        print(f"Проверка: метод {method}, параметр {param}")
        if method == "GET":
            response = requests.get(url, params={"method": param})
        else:
            response = requests.request(method, url, data={"method": param})
        print(response.text)
        print(response.status_code)
        print()
