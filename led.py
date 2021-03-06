#! /usr/bin/env python3
import pigpio

class LED(object):
    ON = 0
    OFF = 1

    LEDs = {
        'RED': 5,
        'YELLOW': 6,
        'GREEN': 13,
    }

    def __init__(self, pi):
        self.pi = pi
        for color, pin in LED.LEDs.items():
            self.pi.set_mode(pin, pigpio.OUTPUT)
            # default off
            self.pi.write(pin, LED.OFF)

    def on(self, color):
        self.pi.write(LED.LEDs[color], LED.ON)

    def off(self, color):
        self.pi.write(LED.LEDs[color], LED.OFF)

    def all_on(self):
        for color in LED.LEDs:
            self.on(color)

    def all_off(self):
        for color in LED.LEDs:
            self.off(color)


# 单例模式
pi = pigpio.pi()
if not pi.connected:
    print('pi is not connected by pigpio daemon')
    exit()
led = LED(pi)

