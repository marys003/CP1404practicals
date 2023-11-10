"""
Emails
Estimate: 30 minutes
Actual:   50 minutes
"""
def split_email(email):
    username = email.split('@')[0]
    split_name = username.split('.')
    name = ' '.join(split_name).title()
    return name

def create_email_dictionary():
    email_dict = {}
    email = input("Email: ")
    while email != "":
        name = split_email(email)
        response = input(f"Is your name {name}? (Y/N) ").upper()
        if response == "" or response == "Y":
            email_dict[email] = name
        else:
            name = input("Name: ").title()
            email_dict[email] = name
        email = input("Email: ")
    return email_dict

def display_email_dictionary(email_dict):
    print("\nEmail dictionary:")
    for email, name in email_dict.items():
        print(f"{name} ({email})")
def main():
    email_dict = create_email_dictionary()
    display_email_dictionary(email_dict)


if __name__ == "__main__":
    main()
