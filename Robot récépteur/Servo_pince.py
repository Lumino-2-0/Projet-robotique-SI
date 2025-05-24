from machine import Pin, PWM

class Servo:
    __servo_pwm_freq = 50
    min_angle = 0
    current_angle = 0.001

    def __init__(self, pin, min=500, max=2500, max_angle=180):
        self.__min_u16_duty = self.__us_to_u16_duty(min)
        self.__max_u16_duty = self.__us_to_u16_duty(max)
        self.max_angle = max_angle
        self.__initialise(pin)

    def stop(self):
        self.__motor.deinit()

    def __angle_to_u16_duty(self, angle):
        return int((angle - self.min_angle) * self.__angle_conversion_factor) + self.__min_u16_duty

    def __us_to_u16_duty(self, us):
        return int(us * 65535 * self.__servo_pwm_freq / 1000000)

    def tourner(self, angle):
        angle = round(angle, 2)
        if angle == self.current_angle:
            return
        self.current_angle = angle
        duty_u16 = self.__angle_to_u16_duty(angle)
        self.__motor.duty_u16(duty_u16)

    def __initialise(self, pin):
        self.current_angle = -0.001
        self.__angle_conversion_factor = (self.__max_u16_duty - self.__min_u16_duty) / (self.max_angle - self.min_angle)
        self.__motor = PWM(Pin(pin))
        self.__motor.freq(self.__servo_pwm_freq)
