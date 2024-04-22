import adafruit_servokit
import numpy

def main():
    print("Servo Menu")
    PIN_CAMERA_SERVO = 11  # unused
    PIN_JOINT_1 = 12
    PIN_JOINT_2 = 13
    PIN_JOINT_3 = 14
    PIN_GRIPPER_SERVO = 15

    servo_kit = adafruit_servokit.ServoKit(channels=16)

    while True:
        print("Pick a servo to move: ")
        print("1 --> Arm Joint 1")
        print("2 --> Arm Joint 2")
        print("3 --> Arm Joint 3")
        print("G --> Gripper")
        selection = input("Selection: ")
        if selection == "":
            servo_kit.servo[PIN_CAMERA_SERVO].angle = None  # Just in case I use it.
            servo_kit.servo[PIN_JOINT_1].angle = None
            servo_kit.servo[PIN_JOINT_2].angle = None
            servo_kit.servo[PIN_JOINT_3].angle = None
            servo_kit.servo[PIN_GRIPPER_SERVO].angle = None
            break
        if selection == "1":
            angle = int(input("Joint 1 DH angle: "))  # flip -90=180 90=0
            angle = numpy.interp(angle, [-90, 90], [180, 0])  # value, given value scale, servo values
            servo_kit.servo[PIN_JOINT_1].angle = angle
        if selection == "2":
            angle = int(input("Joint 2 DH angle: "))  # simple "add 90"
            angle = numpy.interp(angle, [-90, 90], [0, 180])  # value, given value scale, servo values
            servo_kit.servo[PIN_JOINT_2].angle = angle
        if selection == "3":
            angle = int(input("Joint 3 DH angle: "))  # Joint is a simple "add 90"
            angle = numpy.interp(angle, [-90, 90], [0, 180])  # value, given value scale, servo values
            servo_kit.servo[PIN_JOINT_3].angle = angle  # First test NOT mapping
        if selection == "G":
            distance_in = float(input("Gripper open amount (0 to 2 inches): "))
            angle = numpy.interp(distance_in, [0, 2], [120, 20])
            print("Request:", distance_in, " Result: ", angle)
            servo_kit.servo[PIN_GRIPPER_SERVO].angle = angle



main()