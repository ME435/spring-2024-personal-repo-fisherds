import time
import requests

def main():
    print("Plate Loader")

    while True:
        print("0: Exit")
        print("1: RESET")
        print("2: X-AXIS")

        ser = None

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
    res = requests.get('http://localhost:5000/api/' + command)
    print(res.text)


main()
