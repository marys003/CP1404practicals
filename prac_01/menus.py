
MENU = """H - Hello
G - Goodbye
Q - Quit"""
name = input("Enter name : ")
print(MENU)
choice = input(">>> ").lower()
while choice != "q":
    if choice == "h":
        print(F"Hello {name}")
    elif choice == "g":
        print(F"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").lower()
print("Finished.")
