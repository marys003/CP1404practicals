"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion

get menu
choice
while choice not =q
if choice=c
get celcius
fahrenheit = celsius * 9.0 / 5 + 32
    display farenheit
    else if choice=F
get farenheit
celcius = 5 / 9 * (fahrenheit - 32)
display celcius
    else
display error

"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")

    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")