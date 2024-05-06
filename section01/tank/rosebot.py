import rosebot_drive_system
import rosebot_sensors

class RoseBot:
    """ Container for all of the different robot submodules. The top level does nothing."""

    def __init__(self):
        self.drive_system = rosebot_drive_system.DriveSystem()
        self.ultrasonic = rosebot_sensors.UltraSonic()
        self.line_sensors = rosebot_sensors.LineSensors()
        # self.arm_and_claw =