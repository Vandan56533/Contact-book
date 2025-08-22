class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.next = None  # Self-referencing structure

    def __str__(self):
        return f"{self.name},{self.phone},{self.email}"
    from Contact  import Contact

class ContactBook:
    def __init__(self):
        self.head = None

    def insert_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        if self.head is None or name.lower() < self.head.name.lower():
            new_contact.next = self.head
            self.head = new_contact
        else:
            current = self.head
            while current.next and current.next.name.lower() < name.lower():
                current = current.next
            new_contact.next = current.next
            current.next = new_contact

    def search_contact(self, name):
        current = self.head
        while current:
            if current.name.lower() == name.lower():
                return current
            current = current.next
        return None

    def update_contact(self, name, new_phone, new_email):
        contact = self.search_contact(name)
        if contact:
            contact.phone = new_phone
            contact.email = new_email
            return True
        return False

    def delete_contact(self, name):
        current = self.head
        prev = None
        while current:
            if current.name.lower() == name.lower():
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def display_contacts(self):
        current = self.head
        while current:
            print(f"Name: {current.name}, Phone: {current.phone}, Email: {current.email}")
            current = current.next

    def save_to_file(self, filename="contacts.txt"):
        with open(filename, "w") as f:
            current = self.head
            while current:
                f.write(str(current) + "\n")
                current = current.next

    def load_from_file(self, filename="contacts.txt"):
        try:
            with open(filename, "r") as f:
                for line in f:
                    name, phone, email = line.strip().split(",")
                    self.insert_contact(name, phone, email)
        except FileNotFoundError:
            pass
        from contact_book import ContactBook

book = ContactBook()
book.load_from_file()

def menu():
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Show All Contacts")
    print("6. Exit")

while True:
    menu()
    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        book.insert_contact(name, phone, email)
        book.save_to_file()
    elif choice == "2":
        name = input("Search Name: ")
        contact = book.search_contact(name)
        print(contact if contact else "Contact not found.")
    elif choice == "3":
        name = input("Name to update: ")
        phone = input("New Phone: ")
        email = input("New Email: ")
        if book.update_contact(name, phone, email):
            book.save_to_file()
            print("Contact updated.")
        else:
            print("Contact not found.")
    elif choice == "4":
        name = input("Name to delete: ")
        if book.delete_contact(name):
            book.save_to_file()
            print("Contact deleted.")
        else:
            print("Contact not found.")
    elif choice == "5":
        book.display_contacts()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")