from prac_09.silver_service_taxi import SilverServiceTaxi

def main():

    my_silver_taxi = SilverServiceTaxi("Hummer", 200, 4)
    my_silver_taxi.drive(18)

    fare = my_silver_taxi.get_fare()
    print(f"{my_silver_taxi}\nFare: ${fare:.2f}")


if __name__ == "__main__":
    main()
