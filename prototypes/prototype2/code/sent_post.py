import urequests
import json

class HTTPClient:
    def __init__(self):
        pass  # You can add headers or config later

    def send(self, url, data):
        try:
            response = urequests.post(url, json=data)
            result = response.text
            response.close()
            return result
        except Exception as e:
            return {"error": str(e)}
