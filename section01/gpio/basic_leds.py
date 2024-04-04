import gpiozero as gz
import time


def main():
    print("GPIO - Basic LEDs")
    # basic_outputs()
    manual_traffic_light()

def manual_traffic_light():
    print("Manual Traffic Light")
    red_led = gz.LED(14)
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)

    # Loop forever
    #   Green LED on only for 4 seconds
    #   Yellow LED on only for 1 seconds
    #   Red LED on only for 3 seconds

    while True:
        green_led.on()
        time.sleep(4)
        green_led.off()

        yellow_led.on()
        time.sleep(1)
        yellow_led.off()

        red_led.on()
        time.sleep(3)
        red_led.off()


def basic_outputs():
    print("Basic digital output device")
    # red_led = gz.DigitalOutputDevice(14)
    red_led = gz.LED(14)

    for k in range(5):
        red_led.toggle()
        time.sleep(1.0)
        # red_led.on()
        # print("LED on")
        # time.sleep(1.0)
        # red_led.off()
        # print("LED off")
        # time.sleep(1.0)

    print("Goodbye")


main()
