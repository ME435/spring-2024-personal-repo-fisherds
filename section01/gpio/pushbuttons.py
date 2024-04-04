import gpiozero as gz
import time
import signal


def main():
    print("Pushbuttons")
    button_states()
    # TODO: When we get back after break do the Button events with lambda

def button_states():
    print("Reading Button States")
    # When the button is pressed turn on the Red LED
    red_led = gz.LED(14)
    button = gz.Button(25)

    # Example from 14.1.1
    # button.wait_for_press()
    # print("The button was pressed!")

    while True:
        if button.is_pressed:
            red_led.on()
        else:
            red_led.off()

main()
