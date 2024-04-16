import gpiozero as gz
import time


class UltraSonic:

    def __init__(self):
        print("Make the Ultrasonic sensor")
        # From: https://github.com/adeept/Adeept_RaspTank/blob/master/server/ultra.py
        Tr = 11
        Ec = 8
        self.distance_sensor = gz.DistanceSensor(echo=8, trigger=11)

    def get(self):
        return self.distance_sensor.distance


class LineSensors:

    def __init__(self):
        print("Make the line sensors (all 3) as a class")
        line_pin_right = 19
        line_pin_middle = 16
        line_pin_left = 20
        self.left_sensor = gz.LineSensor(line_pin_left)
        self.middle_sensor = gz.LineSensor(line_pin_middle)
        self.right_sensor = gz.LineSensor(line_pin_right)
    
    def get_left(self):
        # 0 should be black
        # 1 should be white
        return self.left_sensor.value
    
    def get_middle(self):
        return self.middle_sensor.value
    
    def get_right(self):
        return self.right_sensor.value



def main():
    print("Local testing for the two sensor types")
    # test_sensor = UltraSonic()
    # while True:
    #     print(f"Distance in meters = {test_sensor.get()}")
    #     time.sleep(2.0)

    test_sensor = LineSensors()
    while True:
        print(f"Left reading = {test_sensor.get_left()}")
        time.sleep(2.0)

if __name__ == "__main__":
    main()
