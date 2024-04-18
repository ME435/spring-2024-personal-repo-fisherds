import adafruit_servokit
import numpy

CHANNEL_JOINT_1 = 12
CHANNEL_JOINT_2 = 13
CHANNEL_JOINT_3 = 14
CHANNEL_GRIPPER = 15


def main():
    print("Servo Menu")

    servo_kit = adafruit_servokit.ServoKit(channels=16)


    while True:
        print("Select a servo:")
        print("1 --> Arm Joint 1")
        print("2 --> Arm Joint 2")
        print("3 --> Arm Joint 3")
        print("G --> Gripper")
        selection = input("Selection: ")
        
        if selection == "":
            servo_kit.servo[CHANNEL_JOINT_1].angle = None
            servo_kit.servo[CHANNEL_JOINT_2].angle = None
            servo_kit.servo[CHANNEL_JOINT_3].angle = None
            servo_kit.servo[CHANNEL_GRIPPER].angle = None
            break
        
        elif selection == "1":
            angle = int(input("Joint 1 angle: "))
            angle = numpy.interp(angle, [-90, 90], [180, 0])
            servo_kit.servo[CHANNEL_JOINT_1].angle = angle
            
        elif selection == "2":
            angle = int(input("Joint 2 angle: "))
            angle = numpy.interp(angle, [-90, 45], [0, 135])  
            servo_kit.servo[CHANNEL_JOINT_2].angle = angle

        elif selection == "3":
            angle = int(input("Joint 3 angle: "))
            angle = numpy.interp(angle, [-90, 90], [0, 180])  
            servo_kit.servo[CHANNEL_JOINT_3].angle = angle
            
        elif selection == "G" or selection == "g":
            inches = float(input("Gripper distance: "))
            angle = numpy.interp(inches, [0, 2], [100, 10])  
            servo_kit.servo[CHANNEL_GRIPPER].angle = angle
        
        else:
            print("Invalid selection")

main()
