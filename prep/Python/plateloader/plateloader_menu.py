import serial
import time


def main():
    print("Plate Loader")

    ser = open_serial()

    while True:
        print("0: Exit")
        print("1: RESET")
        print("2: X-AXIS")

        choice = input("Make a selection: ")
        if choice == "0":
            break
        elif choice == "1":
            send_message(ser, "RESET")
        elif choice == "2":
            to_pos = input("Where to? (1-5): ")
            send_message(ser, f"X-AXIS {to_pos}")
        else:
            print("Unknown command.  Please try again.")


def send_message(ser, command):
    print(f"TODO, send command {command} to the serial object.")
    message_bytes = (command + "\n").encode()
    print(f"Sending the bytes {message_bytes.decode().strip()}")
    ser.write(message_bytes)
    wait_for_response(ser)


# Blocking.  Warning if you call this and nothing comes, it's over!
def wait_for_response(ser):
    while ser.in_waiting == 0:
        time.sleep(0.1)
    print_response(ser)


# Non-blocking, non-waiting, print if you have something
def print_response(ser):
    while ser.in_waiting > 0:
        received = ser.readline()
        print(f"Received: {received.decode().strip()}")


def open_serial(name="/dev/ttyACM0"):
    ser = serial.Serial(name, baudrate=19200)
    print("Connecting... ", end="")
    while not ser.is_open:
        time.sleep(0.1)
    print("Connected")
    time.sleep(1.5)  # optional (really it's for Windows)
    ser.reset_input_buffer()  # optional
    return ser


if __name__ == "__main__":
    main()
