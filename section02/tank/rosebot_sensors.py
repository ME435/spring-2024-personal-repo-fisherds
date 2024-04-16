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


def main():
    print("Local sensor testing")
    test_sensor = UltraSonic()
    while True:
        print(f"Distance = {test_sensor.get_distance()}")
        time.sleep(2.0)

if __name__ == "__main__":
    main()
