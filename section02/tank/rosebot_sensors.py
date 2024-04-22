import gpiozero as gz
import time

class UltraSonic:

    def __init__(self):
        print("Create the ultrasonic")
        # From: https://github.com/adeept/Adeept_RaspTank/blob/master/server/ultra.py
        self.distance_sensor = gz.DistanceSensor(echo=8, trigger=11)

    def get_distance(self):
        return self.distance_sensor.distance


class LineSensors:

    def __init__(self):
        print("Create the 3 line sensors")
        # From: https://github.com/adeept/Adeept_RaspTank/blob/master/server/findline.py
        line_pin_right = 19  # actually this is the left
        line_pin_middle = 16
        line_pin_left = 20   # actually this is the right

        self.left_sensor = gz.LineSensor(line_pin_right)
        self.middle_sensor = gz.LineSensor(line_pin_middle)
        self.right_sensor = gz.LineSensor(line_pin_left)

    def get_left(self):
        # From: https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LineSensor.value
        # This is nearer 0 for black under the sensor <-- Backwards too!
        # nearer 1 for white under the sensor. <-- Backwards too!
        if self.left_sensor.value == 0:
            return "W"
        return "B"

    def get_middle(self):
        if self.middle_sensor.value == 0:
            return "W"
        return "B"
    
    def get_right(self):
        if self.right_sensor.value == 0:
            return "W"
        return "B"
    
def main():
    print("Local sensor testing")
    ultra_sensor = UltraSonic()
    line_sensors = LineSensors()

    while True:
        # print(f"Distance = {ultra_sensor.get_distance()}")
        print(f"Left = {line_sensors.get_left()}  Middle = {line_sensors.get_middle()}  Right = {line_sensors.get_right()}  ")

        time.sleep(2.0)

if __name__ == "__main__":
    main()
