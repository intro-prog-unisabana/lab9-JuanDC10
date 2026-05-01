from aircraft import Aircraft

def main():
    model = input("Enter aircraft model:\n")
    plane = Aircraft(model)

    while True:
        command = input("Enter command (A for ascent, D for descent, X to exit):\n")

        if command == "X":
            break

        parts = command.split()
        if len(parts) != 2:
            continue

        action = parts[0]
        feet = int(parts[1])

        if action == "A":
            plane.climb(feet)
        elif action == "D":
            plane.descend(feet)

    print(f"Final altitude: {plane.altitude} feet")

if __name__ == "__main__":
    main()