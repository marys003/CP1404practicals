user_name = input("Enter name: >  ")
file_name = user_name + ".txt"
out_file = open(file_name, 'w')
out_file.write(user_name)
out_file.close()

text_file = open(file_name,'r')
name = text_file.read()
print(f"Your name is {name}")
text_file.close()

file = "numbers.txt"
numbers = open(file, 'r')
line1 = int(numbers.readline())
line2 = int(numbers.readline())
total = line1 + line2
print(f" The total is {total}")
numbers.close()

numbers = open(file, 'r')
total = 0
for line in numbers:
    number = int(line)
    total = total + number
print(f"the total is {total}")
numbers.close()