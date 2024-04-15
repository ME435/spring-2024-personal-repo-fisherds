import gpiozero as gz 
import time

class Motor:

    def __init__(self, forwards_pin, backwards_pin2, en_pin):
        self.forwards_pin = gz.DigitalOutputDevice(forwards_pin)
        self.backwards_pin2 = gz.DigitalOutputDevice(backwards_pin2)
        self.en_pin = gz.PWMOutputDevice(en_pin)
    
    def go_forwards(self):
        self.forwards_pin.on()
        self.backwards_pin2.off()
        self.en_pin.value = 1.0

def main():
    print("Local Motor testing")
    test_motor = Motor(14, 15, 4)
    test_motor.go_forwards()
    time.sleep(3.0)
    

# If we are running THIS file (not importing it), then run the testing code!
if __name__ == "__main__":
    # TODO: Tomorrow, use this code in another file!
    main()