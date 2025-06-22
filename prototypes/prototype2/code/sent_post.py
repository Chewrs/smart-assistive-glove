import urequests
import json

class HTTPClient:
    def __init__(self):
        pass  # You can add headers or config later

    def send(self, url, data):
        try:
            response = urequests.post(url, json=data)
            print(response.text)
            response.close()
            return True
        except Exception as e:
            print("Error sending data:", e)
            return False