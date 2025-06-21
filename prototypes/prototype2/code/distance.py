from machine import Pin, ADC, time_pulse_us
from time import sleep

trigger = Pin(5, Pin.OUT)
echo = Pin(18, Pin.IN)


def get_distance():
    trigger.off()
    sleep(0.01)
    trigger.on()
    sleep(0.00001)
    trigger.off()
    duration = time_pulse_us(echo, 1, 30000)
    dist = (duration/2)/29.1
    if not dist < 0 or dist > 500:
        return dist
    else:
        return 0

        
buffer = []
while True:
    dist = get_distance()
    print(dist)
    buffer.append(dist)
    
    if len(buffer) >= 20:
        try:
            with open("distance_log.txt", "a") as f:
                for d in buffer:
                    f.write("{:.2f}\n".format(d))
            buffer.clear()
            print('writed'*20)
        except:
            print("Write failed")
    sleep(0.01)