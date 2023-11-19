from prac_09.taxi import Taxi

def main():

    my_taxi=Taxi("Prius 1",100)


    my_taxi.drive(40)
    print(my_taxi)

    #starting a new fare and then drive the car 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)

    # Print the details and the current fare
    print(my_taxi)

if __name__ == "__main__":
    main()
