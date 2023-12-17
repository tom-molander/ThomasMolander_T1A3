import csv

def add_contact(file_name):
    print("Create new contact: ")

    contact_name = input("First Name: ")
    contact_phone = input("Phone: ")
    contact_email = input("Email: ")

    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([contact_name, contact_phone, contact_email])

def delete_contact(file_name):
    pass
        