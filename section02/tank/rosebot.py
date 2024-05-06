import rosebot_drive_system
import rosebot_sensors

class RoseBot:

    def __init__(self):
        self.drive_system = rosebot_drive_system.DriveSystem()
        # self.arm_and_claw =
        self.ultrasonic = rosebot_sensors.UltraSonic()
        self.line_sensors = rosebot_sensors.LineSensors()

