import csv

def add_contact(file_name):
    print("Create new contact: ")

    contact_name = input("Contact Name: ")
    contact_phone = input("Phone: ")
    contact_email = input("Email: ")

    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([contact_name, contact_phone, contact_email])

def delete_contact(file_name):
    
    contact_name = input ("Enter name of contact to delete: ")
    contacts_library = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if (contact_name != row[0]):
                contacts_library.append(row)
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(contacts_library)


def view_contact(file_name):
    print("Here is your contacts library: ")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            print(" ".join(row))


def edit_contact(file_name):
    pass
