def main():
    print("Plate Loader Menu")

    ser = None  # Placeholder today for a Pyserial object

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

def send_message(ser, command):
    print(f"TODO: actually send the command {command} to the serial object.")


main()
