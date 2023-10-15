"""
CP1404/CP5632 Practical
State names in a dictionary
"""
"""
State Names
Estimate: 30 minutes
Actual:   40 minutes
"""

CODE_TO_NAME = { "QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
                 "WA": "Western Australia", "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}


def print_state_name(short_code):
    try:
        name_of_state = CODE_TO_NAME[short_code]
        print(f"{short_code:3s} is {name_of_state}")
    except KeyError:
        print("Invalid short state")


def main():
    for state_code, state_name in CODE_TO_NAME.items():
        print(f"{state_code:3s} is {state_name}")

    state_code = input("Enter short state: ").upper()
    while state_code != "":
        print_state_name(state_code)
        state_code = input("Enter short state: ").upper()


if __name__ == "__main__":
    main()
