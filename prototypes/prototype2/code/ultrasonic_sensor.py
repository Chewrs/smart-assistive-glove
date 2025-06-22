from machine import Pin, time_pulse_us
from time import sleep

class UltrasonicSensor:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger = Pin(trigger_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)
        self.trigger.off()

    def get_distance(self):
        self.trigger.off()
        sleep(0.01)
        self.trigger.on()
        sleep(0.00001)
        self.trigger.off()

        try:
            duration = time_pulse_us(self.echo, 1, 30000)
            dist = (duration / 2) / 29.1  # in cm
            if 0 <= dist <= 500:
                return dist
            else:
                return 0
        except Exception as e:
            print("Distance read error:", e)
            return 0