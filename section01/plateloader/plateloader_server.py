from flask import Flask
from flask import render_template
import serial
import time


app = Flask(__name__)
print("Start the server, don't do serial connection yet!")

# This was great to --debug mode on for web app.

# @app.before_first_request
# def setup_serial():
#     app.ser = open_serial()


@app.route("/")
def mainpage():
    # return "Hello David Fisher!!!!!!"
    return render_template("index.html")


@app.route("/hello/<name>")
def hello_route(name):
    return f"Hello, {name}!"


@app.route("/api/<command>")
def api_route(command):
    return send_message(app.ser, command)
    

def send_message(ser, command):
    print(f"TODO, send command {command} to the serial object.")
    message_bytes = (command + "\n").encode()
    print(f"Sending the bytes {message_bytes.decode().strip()}")
    ser.write(message_bytes)
    return wait_for_response(ser)


# Blocking.  Warning if you call this and nothing comes, it's over!
def wait_for_response(ser):
    while ser.in_waiting == 0:
        time.sleep(0.1)
    return print_response(ser)


# Non-blocking, non-waiting, print if you have something
def print_response(ser):
    while ser.in_waiting > 0:
        received = ser.readline()
        print(f"Received: {received.decode().strip()}")
    return received.decode().strip()


def open_serial(name="/dev/ttyACM0"):
    ser = serial.Serial(name, baudrate=19200)
    print("Connecting... ", end="")
    while not ser.is_open:
        time.sleep(0.1)
    print("Connected")
    time.sleep(1.5)  # optional (really it's for Windows)
    ser.reset_input_buffer()  # optional
    return ser


# Connect on startup.  Has issues with --debug
app.ser = open_serial()