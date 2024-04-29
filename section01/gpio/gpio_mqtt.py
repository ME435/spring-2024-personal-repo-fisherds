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

        if message_type == "yellow":
            if payload == 1:
                self.yellow_led.on()
            if payload == 0:
                self.yellow_led.off()

        if message_type == "green":
            if payload:
                self.green_led.on()
            if not payload:
                self.green_led.off()

        if message_type == "leds":
            if payload[0] == 1:
                self.red_led.on()
            if payload[0] == 0:
                self.red_led.off()
            if payload[1] == 1:
                self.yellow_led.on()
            if payload[1] == 0:
                self.yellow_led.off()
            if payload[2] == 1:
                self.green_led.on()
            if payload[2] == 0:
                self.green_led.off()

def main():
    print("GPIO MQTT")
    app = App()

    # counter = 0
    while True:
        # counter += 1
        # app.mqtt_client.send_message("number", counter)

        time.sleep(2.0)
        app.mqtt_client.send_message("red", "on")
        app.mqtt_client.send_message("yellow", 1)
        app.mqtt_client.send_message("green", True)
        time.sleep(2.0)
        app.mqtt_client.send_message("red", "off")
        app.mqtt_client.send_message("yellow", 0)
        app.mqtt_client.send_message("green", False)
        time.sleep(2.0)
        app.mqtt_client.send_message("leds", [1, 0, 1])
        time.sleep(2.0)
        app.mqtt_client.send_message("leds", [0, 1, 0])

main()
