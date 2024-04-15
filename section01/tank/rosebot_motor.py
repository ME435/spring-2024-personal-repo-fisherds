import gpiozero as gz 
import time

class Motor:

    def __init__(self, forwards_pin, backwards_pin, en_pin):
        self.forwards_pin = gz.DigitalOutputDevice(forwards_pin)
        self.backwards_pin = gz.DigitalOutputDevice(backwards_pin)
        self.en_pin = gz.PWMOutputDevice(en_pin)

    def turn_on(self, speed):
        if speed < -100:
            speed = -100
        if speed > 100:
            speed = 100
        if speed > 0:
            self.forwards_pin.on()
            self.backwards_pin.off()
            self.en_pin.value = speed / 100
        elif speed < 0:
            self.forwards_pin.off()
            self.backwards_pin.on()
            self.en_pin.value = - speed / 100
        else:
            self.forwards_pin.off()
            self.backwards_pin.off()
            self.en_pin.value = 0

    def turn_off(self):
        self.turn_on(0)


def main():
    print("Local Motor testing")
    test_motor = Motor(14, 15, 4)
    test_motor.turn_on(100)
    time.sleep(3.0)
    test_motor.turn_off()
    time.sleep(3.0)
    test_motor.turn_on(-100)
    time.sleep(3.0)
    

# If we are running THIS file (not importing it), then run the testing code!
if __name__ == "__main__":
    # TODO: Tomorrow, use this code in another file!
    main()