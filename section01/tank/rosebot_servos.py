import adafruit_servokit
import numpy

PIN_CAMERA_SERVO = 11  # unused
PIN_JOINT_1 = 12
PIN_JOINT_2 = 13
PIN_JOINT_3 = 14
PIN_GRIPPER_SERVO = 15

class Servos:

    def __init__(self):
        self.servo_kit = adafruit_servokit.ServoKit(channels=16)

    def move_joint_1(self, angle):
        angle = numpy.interp(angle, [-90, 90], [180, 0])  # value, given value scale, servo values
        self.servo_kit.servo[PIN_JOINT_1].angle = angle

    def move_joint_2(self, angle):
        angle = numpy.interp(angle, [-90, 90], [0, 180])  # value, given value scale, servo values
        self.servo_kit.servo[PIN_JOINT_2].angle = angle

    def move_joint_3(self, angle):
        angle = numpy.interp(angle, [-90, 90], [0, 180])  # value, given value scale, servo values
        self.servo_kit.servo[PIN_JOINT_3].angle = angle  # First test NOT mapping

    def move_arm(self, angles):
        angle = numpy.interp(angles[0], [-90, 90], [180, 0])  # value, given value scale, servo values
        self.servo_kit.servo[PIN_JOINT_1].angle = angle

        angle = numpy.interp(angles[1], [-90, 90], [0, 180])  # value, given value scale, servo values
        self.servo_kit.servo[PIN_JOINT_2].angle = angle

        angle = numpy.interp(angles[2], [-90, 90], [0, 180])  # value, given value scale, servo values
        self.servo_kit.servo[PIN_JOINT_3].angle = angle  # First test NOT mapping

    def move_gripper(self, distance_in):
        angle = numpy.interp(distance_in, [0, 2], [120, 20])
        print("Request:", distance_in, " Result: ", angle)
        self.servo_kit.servo[PIN_GRIPPER_SERVO].angle = angle

    def disable(self):
        self.servo_kit.servo[PIN_CAMERA_SERVO].angle = None  # Just in case I use it.
        self.servo_kit.servo[PIN_JOINT_1].angle = None
        self.servo_kit.servo[PIN_JOINT_2].angle = None
        self.servo_kit.servo[PIN_JOINT_3].angle = None
        self.servo_kit.servo[PIN_GRIPPER_SERVO].angle = None

def main():
    print("Testing the servos")
    robot_servos = Servos()

    while True:
        print("Pick a servo to move: ")
        print("1 --> Arm Joint 1")
        print("2 --> Arm Joint 2")
        print("3 --> Arm Joint 3")
        print("G --> Gripper")
        selection = input("Selection: ")
        if selection == "":
            robot_servos.disable()
            break
        if selection == "1":
            angle = int(input("Joint 1 DH angle: "))  # flip -90=180 90=0
            robot_servos.move_joint_1(angle)
        if selection == "2":
            angle = int(input("Joint 2 DH angle: "))  # simple "add 90"
            robot_servos.move_joint_2(angle)
        if selection == "3":
            angle = int(input("Joint 3 DH angle: "))  # Joint is a simple "add 90"
            robot_servos.move_joint_3(angle)
        if selection == "G":
            distance_in = float(input("Gripper open amount (0 to 2 inches): "))
            robot_servos.move_gripper(distance_in)


if __name__ == "__main__":
    main()
    