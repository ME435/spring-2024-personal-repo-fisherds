import rosebot_motor
import time

class DriveSystem:

    def __init__(self):
        Motor_A_EN = 1 # was a 4
        Motor_B_EN = 17
        Motor_A_Pin1 = 14
        Motor_A_Pin2 = 15
        Motor_B_Pin1 = 27
        Motor_B_Pin2 = 18
        self.left_motor = rosebot_motor.Motor(Motor_A_Pin1, Motor_A_Pin2, Motor_A_EN)
        self.right_motor = rosebot_motor.Motor(Motor_B_Pin2, Motor_B_Pin1, Motor_B_EN)

    def go(self, left_speed, right_speed):
        self.left_motor.turn_on(left_speed)
        self.right_motor.turn_on(right_speed)
    
    def stop(self):
        self.left_motor.turn_off()
        self.right_motor.turn_off()

    def go_straight_for_seconds(self, speed, seconds):
        self.go(speed, speed)
        time.sleep(seconds)
        self.stop()
    
    def go_straight_for_inches(self, speed, inches):
        # Convert from inches to seconds
        inches_per_second = 0.05 * speed + 2.15  # Not perfect! Might need to edit this!
        self.go_straight_for_seconds(speed, inches / inches_per_second)
