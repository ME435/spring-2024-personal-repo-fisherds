import serial
import time


def main():
    print("Plate Loader Menu")

    ser = open_serial()  # Placeholder today for a Pyserial object
    # name of the device is /dev/ttyACM0

    while True:
        print("0: Exit")
        print("1: Reset")
        print("2: X-Axis")

        choice = input("Make a selection: ")
        if choice == "0":
            break
        elif choice == "1":
            send_message(ser, "RESET")
        elif choice == "2":
            to_pos = input("To where (1-5): ")
            send_message(ser, f"X-AXIS {to_pos}")
        else:
            print(f"Unknown command {choice}.  Please try again.")


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
    wait_for_response(ser)

# Non-blocking, just print what you've got, always take <0.001 seconds
def print_response(ser):
    while ser.in_waiting > 0:
        received = ser.readline()
        print(f"Received {received.decode().strip()}")

# Blocking, do nothing until I get a reply!
def wait_for_response(ser):
    while ser.in_waiting == 0:
        time.sleep(0.1)
    print_response(ser)

main()
