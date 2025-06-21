import urequests
import json
import network

SSID = "KhunNoo_2.4G"
PASSWORD = "WJ0906560924"

def connect_wifi(SSID,PASSWORD):
    """Connects ESP32 to Wi-Fi and retries on failure."""
    try:
        wifi = network.WLAN(network.STA_IF)
        wifi.active(True)
        wifi.connect(SSID, PASSWORD)

        print("Connecting to Wi-Fi...", end="")
        attempt = 0
        while not wifi.isconnected() and attempt < 20:
            time.sleep(1)
            print(".", end="")
            attempt += 1

        if wifi.isconnected():
            print("\nConnected to:", wifi.ifconfig())
            return wifi.ifconfig()[0]
        else:
            print("\nFailed to connect to Wi-Fi.")
            return None
    except Exception as e:
        print("Wi-Fi Error:", e)
        return None
    
connect_wifi(SSID = "KhunNoo_2.4G",PASSWORD = "WJ0906560924")


url = "http://192.168.1.146:5000/data" 

data = {
    "sensor": "distance",
    "value": 14.33
}

response = urequests.post(url, json=data)
print(response.text)
response.close()
prin