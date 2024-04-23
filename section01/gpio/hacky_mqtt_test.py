import mqtt_helper as mh
import time

def my_first_callback(message_type, payload):
    print("Received the type:", message_type)
    print("Received the payload:", payload)

def main():
    print("Hacky MQTT Test")
    mqtt_client = mh.MqttClient()
    mqtt_client.connect(subscription_topic_name="fisherds",
                        publish_topic_name="fisherds",
                        use_off_campus_broker=True)
    mqtt_client.callback = my_first_callback
    
    counter = 0
    while True:
        time.sleep(2.0)
        counter += 1
        mqtt_client.send_message("number", counter)
        


main()
