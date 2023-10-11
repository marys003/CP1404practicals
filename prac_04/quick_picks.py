
from random import randint


MIN = 1
MAX = 45
QUICK_PICK = 6

number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    numbers = []
    while len(numbers) < QUICK_PICK:
        numbers.append(randint(MIN, MAX))
    numbers = sorted(numbers)
    print("{:2} {:2} {:2} {:2} {:2} {:2}".format(*numbers))