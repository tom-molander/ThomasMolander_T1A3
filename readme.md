# Tom Molander - Terminal Application

### Helpful sources to implement this code:

https://stackoverflow.com/
CoderAcadmey Lessons & Learning Materials

### Soure Control Repository:

https://github.com/tom-molander/ThomasMolander_T1A3

### Code Styling convention:

The program has been adhered too in PEP 8 styling.

https://peps.python.org/pep-0008/

R6 Develop a list of features that will be included in the application. It must include:

### Features

The terminal application contains 5 features including:

- Contacts Library
- Add Contact
- Delete Contact
- View Contacts
- Edit Contact

describe each feature

**Contacts Library** is the primary feature of the terminal application which will print out as list of options as a menu to the user and wait for input from the user. Once input is given from the user this will call for the other features to run and begin to be utilised.

The contacts library will utilise variables known as "user selection", "contacts_file", "file_name" and "selection" while running. Loops and control structure and error handling are all handled through input given from the user, when a user enters a command that is not expected the program will print a message that is doe not recognise that command and loop back to reprint the menu again.

**Add contact** is a feature that is utilised when called by input given from the user using the contacts library feature. When called, the feature will utilise variables "contact_name", "contact_phone" and "contact_email". These will be printed to the terminal to ask for input from the user before storing the data in a csv file. Loops and control structure and error handling are all handled through input given from the user, when data is not given in a numerical range the program will print an error and loop back to ask the user to enter again, until it receives the data in the intended way. It also will apply this for the email input, knowing that an email must contain and "a" symbol.

**Delete Contact** is a feature that is utilised when called by input given from the user using the contacts library feature. When called, the feature will utilise the "contact_name" variable and begin to read the csv file. The function has an new condititon implemented as "contact_found" which is set to False. When reading the file, the feature will use a loop to check if the "contact_name" is in the file, "contact_found" will now be true, the file will append the row and copy the remaining contents and create a new csv file, without the contact_name given. Printing a message to the user that the "Contact_name" has been deleted. The program will handle errors through the "contact_found" True/False statement, where if the "contact_found" is false, the program will print a message to the user that "contact_found" could not be found in the library and begin the loop again.

**View Contacts** is a feature that is utilised when called by input given from the user using the contacts library feature. When called, the feature will read the contents of the csv file and print the contacts list to the terminal for the user. This feature is important for the "Delete Contact" and "Edit Contact" features so that the user can accurately find contacts and what the contact_name is stored as, as well as check if "contact_phone" or "contact_email" are up to date.

**Edit Contact** is a feature that is utilised when called by input given from the user using the contacts library feature. When called, feature will utilise the "contact_name" variable and begin to read the csv file. Similar to the "Delete Contact" has a True or False statement,"contact_found" which is set to False.When reading the file, the feature will use a loop to check if the "contact_name" is in the file, "contact_found" will now be true. If the statement is found to be True the feature will then ask for input for a Phone and email and append the data. If "contact_found" is false, the program will print a message to the user that "contact_found" could not be found in the library and begin the loop again.

### Implementation plan

An implementation plan was created through a trello board. Snippets of progress below:

![Board](Docs/Screenshots/Design_Board_1.png)
![Board](docs/Screenshots/Design%20Board%202.png)
![Board](docs/Screenshots/Design%20Board%203.png)
![Board](docs/Screenshots/Design%20Board%204.png)
![Board](docs/Screenshots/Design%20Board%205.png)
![Board](docs/Screenshots/Design%20Board%206.png)
![Board](docs/Screenshots/Design%20Board%207.png)

### Bash Script

```
#!/bin/bash

#check if python is installed
python3 --version


#check if venv exists
python3 -m venv .venv
#activate virtual environment
source .venv/bin/activate

#packages
pip3 install colored

#To use application
python3 src/main.py
"A" to Add Contact
"D" to Delete Contact
"V to View Contacts
"E" to Edit a Contact"
"C" to close program

```
