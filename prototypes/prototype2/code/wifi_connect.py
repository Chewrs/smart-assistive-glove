import network
import time

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
    


