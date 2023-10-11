print("odds from 1 to 20")
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a.
print("in 10s:")
for i in range(0, 101, 10):
    print(i, end=" ")
print()
#b.
print("from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=" ")
print()
#c.
n = int(input("count stars: "))
print("No. of stars:")
for _ in range(n):
    print("*", end="")
print()