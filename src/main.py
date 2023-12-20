from colored import fg, attr, bg
from functions import add_contact, delete_contact, view_contact, edit_contact

file_name = "contacts.csv"

try: 
    contacts_file = open(file_name, "r")
    contacts_file.close()
except FileNotFoundError:
    contacts_library = open(file_name, "w")
    contacts_library.write("Name, Phone, Email\n")
    contacts_library.close()


print(f"{fg('blue')}{bg('white')}Contact Library")

def contacts_library():
    print(f'{fg('black')}{bg('white')}Enter "A" to add a new contact to your library')
    print(f'{fg('black')}{bg('white')}Enter "D" to delete a contact from your library')
    print(f'{fg('black')}{bg('white')}Enter "V" to view your contacts library')
    print(f'{fg('black')}{bg('white')}Enter "E" to edit a contact')
    print(f'{fg('black')}{bg('white')}Enter "C" to close')

    selection = input("Please enter your selection: ")
    return selection

users_selection = ""

while users_selection != "C":
    users_selection = contacts_library()
    if users_selection == "A":
        add_contact(file_name)
    elif users_selection == "D":
        delete_contact(file_name)
    elif users_selection == "V":
        view_contact(file_name)
    elif users_selection == "E":
        edit_contact(file_name)
    elif users_selection == "C":
        break

    else:
        print(f"{fg('red')}{bg('white')}Sorry, I don't recognise that command. Please try again.{attr('reset')}")

        