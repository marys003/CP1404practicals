import csv
from guitar import Guitar

def load_guitars(file_name):
    guitars = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            name, year, cost = line
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def save_guitars(file_name, guitars):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)

def main():
    file_name = "guitars.csv"
    all_guitars = load_guitars(file_name)

    print("All Guitars:")
    display_guitars(all_guitars)

    all_guitars.sort(key=lambda x: x.year)  # Sort by year
    print("\nSorted Guitars:")
    display_guitars(all_guitars)

    # Ask the user for new guitars
    while True:
        name = input("Enter the name of your guitar (or press Enter to finish): ")
        if not name:
            break
        year = int(input("Enter the year it was made: "))
        cost = float(input("Enter the cost of the guitar: "))
        all_guitars.append(Guitar(name, year, cost))

    # Save the updated list of guitars to the data file
    save_guitars(file_name, all_guitars)

    # Display the updated list of guitars
    print("\nUpdated Guitars:")
    display_guitars(all_guitars)

if __name__ == "__main__":
    main()