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
simple_result = ''
while True:
    
    dist = sensor.get_distance()
    print(dist)
 
    screen.show_text(simple_result,0,10)
    screen.show_text(str(dist),20,33,False)

    
    buffer.append(dist)
    
    
    if len(buffer) >= 5:
        try:
            screen.show_text(str(dist),20,33)
            screen.show_text('sending',0,0,False)

            result = client.send("http://192.168.1.146:5000/data", str(buffer))
            if isinstance(result, dict) and "error" in result:
                simple_result = 'Fail'
                print(result)
            else:
                simple_result ="Success"
                print(result)
            
            print('writed'*20)
            buffer = []
        except:
            simple_result = 'Broken'
    
    
    sleep(0.01)

