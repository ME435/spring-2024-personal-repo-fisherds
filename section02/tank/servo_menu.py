import adafruit_servokit
import numpy

PIN_CAMERA_SERVO = 11
PIN_JOINT_1 = 12
PIN_JOINT_2 = 13
PIN_JOINT_3 = 14
PIN_GRIPPER_SERVO = 15

def main():
    print("Servo menu")

    servo_kit = adafruit_servokit.ServoKit(channels=16)

    while True:
        print("1: Arm Joint 1")
        print("2: Arm Joint 2")
        print("3: Arm Joint 3")
        print("G: Gripper")
        selection = input("Make a selection: ")
        if selection == "":
            servo_kit.servo[PIN_JOINT_1].angle = None
            servo_kit.servo[PIN_JOINT_2].angle = None
            servo_kit.servo[PIN_JOINT_3].angle = None
            servo_kit.servo[PIN_GRIPPER_SERVO].angle = None
            break
        if selection == "1":
            angle = int(input("What DH angle do you want for Joint 1: ")) # flipped
            angle = numpy.interp(angle, [-90, 90], [180, 0])  # value, DH range, servo range
            servo_kit.servo[PIN_JOINT_1].angle = angle
        if selection == "2":
            angle = int(input("What DH angle do you want for Joint 2: ")) # simple add 90
            angle = numpy.interp(angle, [-90, 90], [0, 180])  # value, DH range, servo range
            servo_kit.servo[PIN_JOINT_2].angle = angle
        if selection == "3":
            angle = int(input("What DH angle do you want for Joint 3: ")) # simple add 90
            angle = numpy.interp(angle, [-90, 90], [0, 180])  # value, DH range, servo range
            servo_kit.servo[PIN_JOINT_3].angle = angle
        if selection == "G":
            distance_in = float(input("How wide do you want the gripper (inches): "))
            angle = numpy.interp(distance_in, [0, 2], [120, 20])
            servo_kit.servo[PIN_GRIPPER_SERVO].angle = angle

main()
