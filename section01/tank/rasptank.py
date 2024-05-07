import mqtt_helper as mh
import time
import gpiozero as gz
import datetime
import rosebot

class App:

    def __init__(self):
        print("Setup MQTT and other stuff")
        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.connect(subscription_topic_name="fisherds",
                            publish_topic_name="fisherds",
                            use_off_campus_broker=True)
        self.mqtt_client.callback = self.mqtt_callback

        self.robot = rosebot.RoseBot()
        self.is_streaming_line_sensors = False
        self.is_driving_until_wall = False
        self.is_driving_until_line = False
        self.is_line_following = False

    def mqtt_callback(self, message_type, payload):
        print("Type:", message_type)
        print("Payload:", payload)

        if message_type == "is_streaming_line_sensors":
            self.is_streaming_line_sensors = payload

        if message_type == "drive":
            left_speed = payload[0]
            right_speed = payload[1]
            self.robot.drive_system.go(left_speed, right_speed)
        
        if message_type == "mode":
            if payload == "drive_until_wall":
                self.is_driving_until_wall = True
                self.robot.drive_system.go(70, 70)
        
        if message_type == "mode":
            if payload == "drive_until_line":
                self.is_driving_until_line = True
                self.robot.drive_system.go(70, 70)

def main():
    print("RaspTank")
    app = App()

    last_sent_time_s = 0

    # Test to talk to myself
    # time.sleep(0.5)
    # app.mqtt_client.send_message("is_streaming_line_sensors", False)

    while True:
        time.sleep(0.1)
        
        if app.is_driving_until_wall:
            if app.robot.ultrasonic.get() < 0.2:
                app.robot.drive_system.stop()
                app.is_driving_until_wall = False
        
        if app.is_driving_until_line:
            if app.robot.line_sensors.is_line():
                app.robot.drive_system.stop()
                app.is_driving_until_line = False

        if app.is_streaming_line_sensors:
            now = datetime.datetime.now() # current date and time
            if now.timestamp() - last_sent_time_s > 2:
                last_sent_time_s = now.timestamp()  # It's time to do another send!
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

                wb_left = app.robot.line_sensors.get_left()
                wb_middle = app.robot.line_sensors.get_middle()
                wb_right = app.robot.line_sensors.get_right()

                app.mqtt_client.send_message("line_sensor_reading", {"timestamp": date_time,
                                                                    "left": wb_left,
                                                                    "middle": wb_middle,
                                                                    "right": wb_right})


main()
