import gpiozero as gz
import time

Motor_A_EN = 4
Motor_B_EN = 17

Motor_A_Pin1 = 14
Motor_A_Pin2 = 15
Motor_B_Pin1 = 27
Motor_B_Pin2 = 18

def main():
    print("Quick Motor Test")

    right_motor_backwards_pin = gz.DigitalOutputDevice(Motor_B_Pin1)
    right_motor_forwards_pin = gz.DigitalOutputDevice(Motor_B_Pin2)
    right_motor_pwm_enable = gz.PWMOutputDevice(Motor_B_EN)

    left_motor_backwards_pin = gz.DigitalOutputDevice(Motor_A_Pin2)
    left_motor_forwards_pin = gz.DigitalOutputDevice(Motor_A_Pin1)
    left_motor_pwm_enable = gz.PWMOutputDevice(Motor_A_EN)

    # # Make BOTH motors go forwards for 3 seconds
    # print("Both forwards")
    # right_motor_forwards_pin.on()
    # right_motor_backwards_pin.off()
    # right_motor_pwm_enable.value = 1.0

    # left_motor_forwards_pin.on()
    # left_motor_backwards_pin.off()
    # left_motor_pwm_enable.value = 1.0

    # time.sleep(3)

    # # Make the JUST the right motor go forwards for 3 seconds
    # print("Just right forwards")
    # right_motor_forwards_pin.on()
    # right_motor_backwards_pin.off()
    # right_motor_pwm_enable.value = 1.0

    # left_motor_forwards_pin.off()
    # left_motor_backwards_pin.off()
    # left_motor_pwm_enable.value = 0.0

    # time.sleep(3)

    # # Make the JUST the left motor go forwards for 3 seconds
    # print("Just left forwards")
    # right_motor_forwards_pin.off()
    # right_motor_backwards_pin.off()
    # right_motor_pwm_enable.value = 0.0

    # left_motor_forwards_pin.on()
    # left_motor_backwards_pin.off()
    # left_motor_pwm_enable.value = 1.0

    # time.sleep(3)

    
    # # Make BOTH motors go backwards for 3 seconds
    # print("Both backwards")
    # right_motor_forwards_pin.off()
    # right_motor_backwards_pin.on()
    # right_motor_pwm_enable.value = 1.0

    # left_motor_forwards_pin.off()
    # left_motor_backwards_pin.on()
    # left_motor_pwm_enable.value = 1.0

    # time.sleep(3)

    # # Make the JUST the right motor go backwards for 3 seconds
    # print("Just right backwards")
    # right_motor_forwards_pin.off()
    # right_motor_backwards_pin.on()
    # right_motor_pwm_enable.value = 1.0

    # left_motor_forwards_pin.off()
    # left_motor_backwards_pin.off()
    # left_motor_pwm_enable.value = 0.0

    # time.sleep(3)

    # # Make the JUST the left motor go backwards for 3 seconds
    # print("Just left backwards")
    # right_motor_forwards_pin.off()
    # right_motor_backwards_pin.off()
    # right_motor_pwm_enable.value = 0.0

    # left_motor_forwards_pin.off()
    # left_motor_backwards_pin.on()
    # left_motor_pwm_enable.value = 1.0

    # time.sleep(3)
    
    # Spin CW for 3 seconds
    print("Spin for 3 seconds CW")
    right_motor_forwards_pin.off()
    right_motor_backwards_pin.on()
    right_motor_pwm_enable.value = 1.0

    left_motor_forwards_pin.on()
    left_motor_backwards_pin.off()
    left_motor_pwm_enable.value = 1.0

    time.sleep(3)

    # Spin CCW for 3 seconds
    print("Spin for 3 seconds CCW")
    right_motor_forwards_pin.on()
    right_motor_backwards_pin.off()
    right_motor_pwm_enable.value = 1.0

    left_motor_forwards_pin.off()
    left_motor_backwards_pin.on()
    left_motor_pwm_enable.value = 1.0

    time.sleep(8)

    right_motor_forwards_pin.off()
    right_motor_backwards_pin.off()
    right_motor_pwm_enable.value = 0.0





main()
