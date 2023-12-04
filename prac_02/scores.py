import random
def main():
    try:
        score = float(input("Enter score: "))
        print(calculate_score(score))
    except ValueError:
        print("Invalid input! Please enter a valid score.")
    random_score = random.randint(0, 100)
    print(f"Random Score : {random_score} Result: {calculate_score(random_score)}")

def calculate_score(score):
    if score < 0 or score > 100:
        return "Invalid Score! Enter a score between 0 and 100"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"

main()