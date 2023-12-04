#importing the prev files
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def choose_taxi(taxis):
    display_taxis(taxis)
    choice = input("Choose taxi: ")
    try:
        choice = int(choice)
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input. Please enter a number.")

def drive_taxi(taxi):
    """Drive the chosen taxi."""
    if taxi is None:
        print("You need to choose a taxi before you can drive")
        return None
    else:
        distance = float(input("Drive how far? "))
        fare = taxi.drive(distance)
        print(f"Your {taxi.name} trip cost you ${fare:.2f}")
        return fare

def main():
    current_taxi = None
    total_bill = 0
    taxis = [Taxi("Prius", 123), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")

    while True:
        print(f"Bill to date: ${total_bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == 'q':
            break
        elif choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            fare = drive_taxi(current_taxi)
            if fare is not None:
                total_bill += fare
        else:
            print("Invalid option")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

if __name__ == "__main__":
    main()
