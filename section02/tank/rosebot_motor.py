import gpiozero as gz
import time

class Motor:

    def __init__(self, forwards_gpio, backwards_gpio, enable_gpio):
        print("Create a Motor")
        self.forwards_pin = gz.DigitalOutputDevice(forwards_gpio)
        self.backwards_pin = gz.DigitalOutputDevice(backwards_gpio)
        self.pwm_enable = gz.PWMOutputDevice(enable_gpio)
    
    def turn_on(self, speed):
        if speed > 100:
            speed = 100
        if speed < -100:
            speed = -100
        if speed > 0:
            self.forwards_pin.on()
            self.backwards_pin.off()
            self.pwm_enable.value = speed / 100
        elif speed < 0:
            self.forwards_pin.off()
            self.backwards_pin.on()
            self.pwm_enable.value = - speed / 100
        else:
            self.forwards_pin.off()
            self.backwards_pin.off()
            self.pwm_enable.value = 0

    def turn_off(self):
        self.turn_on(0)


def main():
    print("Local testing of the Motor class")
    Motor_A_EN = 4
    Motor_B_EN = 17

    Motor_A_Pin1 = 14
    Motor_A_Pin2 = 15
    Motor_B_Pin1 = 27
    Motor_B_Pin2 = 18
    test_motor = Motor(Motor_B_Pin2, Motor_B_Pin1, Motor_B_EN)
    # test_motor = Motor(Motor_A_Pin1, Motor_A_Pin2, Motor_A_EN)
    test_motor.turn_on(-100)
    time.sleep(3.0)
    test_motor.turn_off()

if __name__ == "__main__":
    main()
