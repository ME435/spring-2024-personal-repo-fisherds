import mqtt_helper as mh
import time
import gpiozero as gz

class App:

    def __init__(self):
        print("Using MQTT with a class")

        self.red_led = gz.LED(14)
        self.yellow_led = gz.LED(15)
        self.green_led = gz.LED(18)

        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.connect(subscription_topic_name="me435/fisherds",
                            publish_topic_name="me435/fisherds",
                            use_off_campus_broker=False)
        self.mqtt_client.callback = self.mqtt_callback

    def mqtt_callback(self, message_type, payload):
        print("Received type:", message_type)
        print("Received payload:", payload)

        if message_type == "red":
            if payload == "on":
                self.red_led.on()
            if payload == "off":
                self.red_led.off()
        if message_type == "green":
            if payload:  # for fun I sent True for on and False for off
                self.green_led.on()
            else:
                self.green_led.off()
        if message_type == "leds":
            if payload[0] == 1:
                self.red_led.on()
            else:
                self.red_led.off()

            if payload[1] == 1:
                self.yellow_led.on()
            else:
                self.yellow_led.off()

            if payload[2] == 1:
                self.green_led.on()
            else:
                self.green_led.off()


def main():
    print("GPIO MQTT")
    app = App()
    time.sleep(1.5)  # a short delay to allow MQTT to connect before sending stuff.

    while True:
        # time.sleep(0.1)

        print("Sending red on")
        app.mqtt_client.send_message("red", "on")
        time.sleep(2.0)
        print("sending red off")
        app.mqtt_client.send_message("red", "off")
        
        

        # print("Sending red on")
        # app.mqtt_client.send_message("red", "on")
        # app.mqtt_client.send_message("green", True)
        # time.sleep(2.0)
        # print("sending red off")
        # app.mqtt_client.send_message("red", "off")
        # app.mqtt_client.send_message("green", False)
        # time.sleep(2.0)
        # app.mqtt_client.send_message("leds", [0, 1, 0])
        # time.sleep(2.0)
        # app.mqtt_client.send_message("leds", [1, 0, 1])
        # time.sleep(2.0)
        # app.mqtt_client.send_message("leds", [0, 0, 0])
        # time.sleep(2.0)


main()