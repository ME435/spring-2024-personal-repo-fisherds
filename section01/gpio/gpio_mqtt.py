import mqtt_helper as mh
import time
import gpiozero as gz

class App:

    def __init__(self):
        print("Setup MQTT and other stuff")
        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.connect(subscription_topic_name="fisherds",
                            publish_topic_name="fisherds",
                            use_off_campus_broker=False)
        self.mqtt_client.callback = self.mqtt_callback

        # Get out of the virtual environment to use gpiozero
        self.red_led = gz.LED(14)
        self.yellow_led = gz.LED(15)
        self.green_led = gz.LED(18)
        

    def mqtt_callback(self, message_type, payload):
        print("Type:", message_type)
        print("Payload:", payload)
        # TODO: Actually do something with the message!

        if message_type == "red":
            if payload == "on":
                self.red_led.on()
            if payload == "off":
                self.red_led.off()

def main():
    print("GPIO MQTT")
    app = App()

    # counter = 0
    while True:
        time.sleep(2.0)
        # counter += 1
        # app.mqtt_client.send_message("number", counter)
        app.mqtt_client.send_message("red", "on")
        time.sleep(2.0)
        app.mqtt_client.send_message("red", "off")

main()
