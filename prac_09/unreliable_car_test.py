from prac_09.unreliable_car import UnreliableCar

def main():

    my_unreliable_car = UnreliableCar("Unreliable", 100, 50)

    distance_driven = my_unreliable_car.drive(30)

    print(f"{my_unreliable_car}\nDistance driven: {distance_driven} km")

if __name__ == "__main__":
    main()
