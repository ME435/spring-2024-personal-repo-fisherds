import gpiozero as gz
import time

Motor_A_EN    = 4
Motor_B_EN    = 17

Motor_A_Pin1  = 14
Motor_A_Pin2  = 15
Motor_B_Pin1  = 27
Motor_B_Pin2  = 18


def main():
    print("Quick Motor Test")

    # Goal is to make both motors go forwards for 3 seconds!
    left_forward_pin = gz.DigitalOutputDevice(Motor_A_Pin1)
    left_backward_pin = gz.DigitalOutputDevice(Motor_A_Pin2)
    left_enable_pin = gz.PWMOutputDevice(Motor_A_EN)

    right_forward_pin = gz.DigitalOutputDevice(Motor_B_Pin2)
    right_backward_pin = gz.DigitalOutputDevice(Motor_B_Pin1)
    right_enable_pin = gz.PWMOutputDevice(Motor_B_EN)

    left_forward_pin.on()
    left_backward_pin.off()
    left_enable_pin.value = 1.0

    right_forward_pin.on()
    right_backward_pin.off()
    right_enable_pin.value = 1.0
    time.sleep(3.0)

main()
