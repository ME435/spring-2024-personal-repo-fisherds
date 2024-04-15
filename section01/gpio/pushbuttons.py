import gpiozero as gz
import time
import signal


def main():
    print("Pushbuttons")
    # button_states()
    button_events()

def say_hello():
    print("Hello")

def say_goodbye():
    print("Goodbye")

def turn_leds_on(r, y, g):
    r.on()
    y.on()
    g.on()

def turn_leds_off(r, y, g):
    r.off()
    y.off()
    g.off()


def say_hello_names(names):
    for name in names:
        print("Hello", name)


def button_events():
    print("Button Events")
    red_led = gz.LED(14)
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)
    button = gz.Button(25)

    # red_led.blink()

    # button.when_pressed = say_hello
    # button.when_released = say_goodbye
    # button.when_pressed = lambda : turn_leds_on(red_led, yellow_led, green_led)
    # button.when_released = lambda : turn_leds_off(red_led, yellow_led, green_led)

    my_names = []
    button.when_pressed = lambda : my_names.append("David")
    button.when_released = lambda : say_hello_names(my_names)


    signal.pause()




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
