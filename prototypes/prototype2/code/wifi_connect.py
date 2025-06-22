import network
import time

class WiFiManager:
    def __init__(self):
        self.wifi = network.WLAN(network.STA_IF)
        self.wifi.active(True)

    def connect(self, ssid, password, max_attempts=20):
        print("Connecting to Wi-Fi...", end="")
        self.wifi.connect(ssid, password)

        attempt = 0
        while not self.wifi.isconnected() and attempt < max_attempts:
            time.sleep(1)
            print(".", end="")
            attempt += 1

        if self.wifi.isconnected():
            print("\nConnected to:", self.wifi.ifconfig())
            return self.wifi.ifconfig()[0]
        else:
            print("\nFailed to connect to Wi-Fi.")
            return None

    def is_connected(self):
        return self.wifi.isconnected()

    def disconnect(self):
        if self.wifi.isconnected():
            self.wifi.disconnect()
            print("Disconnected from Wi-Fi.")