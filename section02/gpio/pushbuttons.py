import gpiozero as gz
import time


def main():
    print("Pushbuttons")
    buttons_using_states()
    
def buttons_using_states():
    print("Button States")
    # Turn the LED on when the button pressed, otherwise off
    button = gz.Button(25)
    red_led = gz.LED(14)

    while True:
        if button.is_pressed:
            red_led.on()
        else:
            red_led.off()


main()
