def main():
    password = accept_input()
    asterisks = display_stars(password)
    print(asterisks)



def display_stars(password):
    return '*' * len(password)

def accept_input():
    password = input("Enter password : ")
    return password


main()
