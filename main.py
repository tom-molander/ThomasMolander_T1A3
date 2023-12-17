from functions import add_contact, view_contact

file_name = "contacts.csv"

try: 
    contacts_file = open(file_name, "r")
    contacts_file.close()
except:
    print("Block")

print ("Contact Library")

def contacts_library():
    print('Enter "A" to add a new contact to your library')
    print('Enter "D" to delete a contact from your library')
    print('Enter "V" to view your contacts library')
    print('Enter "E" to edit a contact')
    print('Enter "C" to close')

    selection = input("Please enter your selection: ")
    return selection


users_selection = ""

while users_selection != "C":
    users_selection = contacts_library()
    if (users_selection == "A"):
        add_contact(file_name)

    elif (users_selection == "D"):
        print("Hello World")

    elif (users_selection == "V"):
        print ("View Contact")

    elif (users_selection == "E"):
        print("Enter contact name you want to edit")
    elif (users_selection =="C"):
        break
    else: 
        print ("Sorry I don't recognise that command, can you try again?")

        