"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A) When user enters in non-numeric  value
2. When will a ZeroDivisionError occur?
A) When user try to divide a number by zero, that is denominator is equal to 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        denominator = int(input("Enter the denominator(not 0): "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
    denominator = int(input("Enter the denominator(not 0): "))
    fraction = numerator / denominator
    print(fraction)
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
