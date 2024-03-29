from flask import Flask
from flask import render_template
import serial
import time

app = Flask(__name__)
# print("Note: The Serial connect doesn't happen until the first request")

# @app.before_first_request
# def setup_serial():
#     app.ser = open_serial()


@app.route("/")
def mainpage():
    return render_template("index.html")


@app.route("/hello/<name>")
def hello_route(name):
    return f"Hello, {name}! Thanks for visiting!"


@app.route("/api/<command>")
def api_route(command):
    return send_message(app.ser, command)


def open_serial(name="/dev/ttyACM0"):
    print("Connecting... ", end="")
    ser = serial.Serial(name, baudrate=19200)
    while not ser.is_open:
        time.sleep(0.1)
    time.sleep(1.5)  # Option (for the tank sometimes it's good to wait a moment)
    ser.reset_input_buffer()  # optional
    print("Connected")
    return ser


def send_message(ser, command):
    print(f"TODO: actually send the command {command} to the serial object.")
    message_bytes = (command + "\n").encode()
    print(f"Sending the bytes {message_bytes.decode().strip()}")
    ser.write(message_bytes)
    return wait_for_response(ser)

# Non-blocking, just print what you've got, always take <0.001 seconds
def print_response(ser):
    while ser.in_waiting > 0:
        received = ser.readline()
        print(f"Received {received.decode().strip()}")
    return received.decode().strip()

# Blocking, do nothing until I get a reply!
def wait_for_response(ser):
    while ser.in_waiting == 0:
        time.sleep(0.1)
    return print_response(ser)

# Better: Connects to the serial object right away!
# Worse: does not play nicely with --debug
app.ser = open_serial()
