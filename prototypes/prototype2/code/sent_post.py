import urequests
import json


def sent(url, data): 
    try:
        response = urequests.post(url, json=data)
        print(response.text)
        response.close()
    except Exception as e:
        print("Error sending data:", e)
        

