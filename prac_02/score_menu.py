
MENU = """
(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars 
(Q)uit
"""


def get_valid_score():
    while True:
        try:
            score = int(input("Enter score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid Score! Enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a valid score.")


def calculate_result(score):
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


def print_stars(score):
    stars = '*' * score
    return "\n" + stars


def main():
    print(MENU)
    while True:
        choice = input(">>> ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
                result = calculate_result(score)
                print(result)
        elif choice == "S":
                stars = print_stars(score)
                print(stars)
        elif choice == "Q":
            break
        else:
            print("Invalid option")

    print("Good Bye!")


if __name__ == "__main__":
    main()
