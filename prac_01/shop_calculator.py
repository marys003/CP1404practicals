number_of_items = int(input("Enter number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Enter number of items: "))
total = 0
count = 0
while count < number_of_items:
    price = float(input("Price of item: $"))
    total += price
    count = count + 1
if total > 100:
    discount = total * 0.1
    total = total - discount
print(F"Total price for {number_of_items} items is ${total:.2f}")