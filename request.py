import requests


def ask():
    url = "http://localhost:5005/webhooks/rest/webhook"
    data = {"sender": "User", "message": "Hello"}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        parsed_data = response.json()

    print(parsed_data)

    return "ok"


ask()
