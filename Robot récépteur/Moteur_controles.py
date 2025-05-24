from machine import Pin, PWM

class Moteur:
    def __init__(self, ena, in1, in2):
        self.ena = PWM(Pin(ena))
        self.ena.freq(1000)
        self.in1 = Pin(in1, Pin.OUT)
        self.in2 = Pin(in2, Pin.OUT)

    def avancer(self, vitesse=50000):
        self.in1.value(1)
        self.in2.value(0)
        self.ena.duty_u16(vitesse)

    def reculer(self, vitesse=50000):
        self.in1.value(0)
        self.in2.value(1)
        self.ena.duty_u16(vitesse)

    def stop(self):
        self.ena.duty_u16(0)
        self.in1.value(0)
        self.in2.value(0)
