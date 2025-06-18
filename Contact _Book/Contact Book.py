contacts = []

def add_contacts():
    print("\n➖➖➖ Add New Contact ➖➖➖📱📕")
    name = input("Enter The Name: ")
    phone = input("Enter The Contact Numeber: ")
    email = input("Enter The Contact Email: ")

    new_contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts.append(new_contact)
    print(f" {name} added!😁")

def view_contacts():
    print("\n➖➖➖Your Contacts➖➖➖")
    if not contacts:
        print("No contacts found.⛔")
        return
    for i, contact in enumerate(contacts):
        print(f"\n{i+1}. Name: {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email'] if contact['email'] else 'N/A'}")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")

def display_menu():
    print("\n➖➖➖ Menu ➖➖➖")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")
    print("➖➖➖➖➖➖➖➖➖➖")

def main():
    while True:
        display_menu()
        choice = input("Enter Your Choice (1-3): ")

        if choice == '1':
            add_contacts()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            print("GoodBye!!👋👋")
            break
        else:
            print("Invaild choice. Please try again.")

if __name__ == "__main__":
    main()