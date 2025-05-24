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

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
redirect_count = len(response.history)
final_url = response.url
print(f"Количество редиректов: {redirect_count}")
print(f"Конечный URL: {final_url}")
