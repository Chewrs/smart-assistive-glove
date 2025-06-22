from machine import Pin, ADC, time_pulse_us
from time import sleep

from sent_post import HTTPClient
from wifi_connect import WiFiManager
from display import  OLEDDisplay
from ultrasonic_sensor import UltrasonicSensor

#display
screen = OLEDDisplay()
client = HTTPClient()

#wifi
SSID = "KhunNoo_2.4G"
PASSWORD = "WJ0906560924"

wifi = WiFiManager()
wifi.connect(SSID, PASSWORD)

#Ultrasonic Sensor
sensor = UltrasonicSensor(trigger_pin=5, echo_pin=18)  # change pins as needed


        
buffer = []
while True:
    
    dist = sensor.get_distance()
    print(dist)
 
    screen.show_text(str(dist))
    
    buffer.append(dist)
    
    
    if len(buffer) >= 20:
        try:
            screen.show_text('sending')


            client.send("http://192.168.1.146:5000/data", str(buffer))

            print('writed'*20)
            screen.show_text('sent')
            buffer = []
        except:
            print("Write failed")
            screen.show_text('sent fail')
    
    
    sleep(0.01)

