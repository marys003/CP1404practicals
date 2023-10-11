import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# 9
# What was the smallest number you could have seen, what was the largest?
# smallest 5 and largest 20

# What did you see on line 2?
# 5

# What was the smallest number you could have seen, what was the largest?
# smallest 3 and largest 9

# Could line 2 have produced a 4?
# no

# What did you see on line 3?
# 5.384705533773956
# What was the smallest number you could have seen, what was the largest?
# smallest 2.5 and largest 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))