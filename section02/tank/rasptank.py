import mqtt_helper as mh
import time
import gpiozero as gz
import datetime
import rosebot

class App:

    def __init__(self):
        print("Using MQTT with a class")

        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.connect(subscription_topic_name="fisherds",
                            publish_topic_name="fisherds",
                            use_off_campus_broker=True)
        self.mqtt_client.callback = self.mqtt_callback

        self.robot = rosebot.RoseBot()
        self.is_streaming = False
        self.drive_until_wall = False
        self.drive_until_line = False
        self.is_line_following = False


    def mqtt_callback(self, message_type, payload):
        print("Received type:", message_type)
        print("Received payload:", payload)
        
        if message_type == "is_streaming":
            self.is_streaming = payload
            
        if message_type == "drive":
            self.robot.drive_system.go(payload[0], payload[1])
            
        if message_type == "mode":
            if payload == "drive_until_wall":
                self.drive_until_wall = True
                self.robot.drive_system.go(90, 90)            

                
def main():
    print("RaspTank")
    app = App()

    last_time_sent_s = 0
    
    # Purely as a talking to myself test, turn on sensor streaming
    # time.sleep(0.5)  # allow mqtt to connect
    # app.mqtt_client.send_message("is_streaming", True)
    
    while True:
        time.sleep(0.1)
        
        if app.drive_until_wall:
            if app.robot.ultrasonic.get_distance() < 0.2:
                app.robot.drive_system.stop()
                app.drive_until_wall = False
        
        now = datetime.datetime.now() # current date and time
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        timestamp_s = now.timestamp()

        if timestamp_s - last_time_sent_s > 2 and app.is_streaming:
            last_time_sent_s = timestamp_s
            app.mqtt_client.send_message("line_sensor_reading", 
                                        {"timestamp": date_time,
                                        "left": app.robot.line_sensors.get_left(),
                                        "middle": app.robot.line_sensors.get_middle(),
                                        "right": app.robot.line_sensors.get_right()})





main()