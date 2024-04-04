import gpiozero as gz
import time
import signal


def main():
    print("GPIO - Fancy LEDs")
    # fancy_blink()
    # pwm_led()
    # led_board()
    fancy_traffic_light()

def fancy_traffic_light():
    print("Fancy Traffic Light")

    # Loop forever
    #   Green LED on only for 4 seconds
    #   Yellow LED on only for 1 seconds
    #   Red LED on only for 3 seconds

    # BUT this time use the fancy class TrafficLights!
    lights = gz.TrafficLights(14, 15, 18)

    while True:
        lights.green.on()
        time.sleep(4)
        lights.green.off()

        lights.yellow.on()
        time.sleep(1)
        lights.yellow.off()

        lights.red.on()
        time.sleep(3)
        lights.red.off()


def led_board():
    print("LED Board")

    # Make an LEDBoard with all 3 LEDs
    board = gz.LEDBoard(14, 15, 18, pwm=True)

    # Loop Forever
    #   Turn on all LEDs
    #   1 second
    #   Turn on just red and green
    #   1 second
    #   Turn off all LEDs
    #   1 second

    while True:
        board.on()
        time.sleep(1.0)
        board.value = (1, 0, 1)
        time.sleep(1.0)
        # Keep Red and Green at full brighness, but make yellow on dim.
        board.value = (1, 0.3, 1)
        time.sleep(1.0)
        
        board.off()
        time.sleep(1.0)
        


def pwm_led():
    print("PWM Control an LED")
    red_pwm = gz.PWMLED(14)

    # Loop forever
    #   Slowly get brighter up to max (3 seconds)
    #   Slowly get slower down to 0 (3 seconds)

    while True:
        for k in range(30):
            red_pwm.value = k / 30
            print("Up", red_pwm.value)
            time.sleep(0.1)

        for k in range(30):
            red_pwm.value = (30 - k) / 30
            time.sleep(0.1)
            print("Down", red_pwm.value)




def fancy_blink():
    print("Fancy Blink")
    red_led = gz.LED(14)

    red_led.blink(on_time=0.5, off_time=0.1)
    signal.pause()
    print("Goodbye")

main()