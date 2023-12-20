import csv
from colored import fg, attr, bg



def add_contact(file_name):
    print(f"{fg('green')}{bg('white')}Create new contact:")

    contact_name = input(f"{fg('black')}{bg('white')}Contact Name:")
    while True:
        contact_phone = input(f"{fg('black')}{bg('white')}Phone: ")
        if contact_phone.isdigit():
            break
        else: 
            print(f"{fg('red')}{bg('white')}Phone number must be entered in numbers")
    while True:
        contact_email = input(f"{fg('black')}{bg('white')}Email: ")
        if "@" in contact_email:
            break
        else: 
            print(f'{fg('red')}{bg('white')}Email must contain "@" symbol, please enter again')
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([contact_name, contact_phone, contact_email])

    print(f"{fg('green')}{bg('white')}'{contact_name}' has been added to your contacts library")


def delete_contact(file_name):
    contact_name = input(f"{fg('green')}{bg('white')}Enter name of contact to delete: ")
    contacts_library = []
    contact_found = False

    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0 and contact_name == row[0]:
                contact_found = True
            else:
                contacts_library.append(row)

    if contact_found:
        with open(file_name, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(contacts_library)

        print(f"{fg('green')}{bg('white')}'{contact_name}' has been deleted.")
    else:
        print(f"{fg('red')}{bg('white')}Could not find '{contact_name}' in your library.")




def view_contact(file_name):
    print(f"{fg('green')}{bg('white')}Here is your contacts library: ")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            print(" ".join(row))



def edit_contact(file_name):
    contact_name = input(f"{fg('green')}{bg('white')}Enter name of contact to edit: ")
    contacts_library = []
    contact_found = False

    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0 and contact_name != row[0]:
                contacts_library.append(row)
            elif len(row) > 0:
                updated_row = [contact_name, input(f"{fg('black')}{bg('white')}Enter new phone number: "), input(f"{fg('black')}{bg('white')}Enter new email: ")]
                contacts_library.append(updated_row)
                contact_found = True

                
    with open(file_name, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(contacts_library)

        if contact_found:
            print(f"{fg('green')}{bg('white')}'{contact_name}' has been updated.")
        else:
            print(f"{fg('red')}{bg('white')}Could not find '{contact_name}' in your library.")

