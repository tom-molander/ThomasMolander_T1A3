import csv

def add_contact(file_name):
    print("Create new contact: ")

    contact_first_name = input("First Name: ")
    contact_surname = input("Surname: ")
    contact_phone = input("Phone: ")
    contact_email = input("Email: ")

    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([contact_first_name, contact_surname, contact_phone, contact_email])
