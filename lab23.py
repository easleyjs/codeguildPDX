"""
Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together,
and go over how to load that file. Headers might consist of name, favorite fruit, favorite color.
Open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user.
The text in the header represents the keys, the text in the other lines represent the values.

Implement a CRUD REPL

Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.

"""


def getContactsFromFile(contactsFile):
    with open(contactsFile, 'r') as file:
        lines = file.read().split('\n')
    header = lines[0].split(',')
    return [dict(zip(header, lines[i].split(","))) for i in range(1, len(lines))]


def contactSearch(contacts, contactName):
    for i in range(len(contacts)):
        if contacts[i]['name'] == contactName:
            return i


def createContact(contacts):
    print(f"{'*'*30} New Contact {'*'*30}")
    contactName = input("Contact Name: ")
    contactEmail = input("Contact Email: ")
    contactPhone = input("Contact Phone: ")
    # contactDict = dict()
    contacts.append({'name': contactName, 'email': contactEmail, 'phone': contactPhone})
    return contacts


def retrieveContact(contacts, contactName):
    contactId = contactSearch(contacts, contactName)
    if contactId:
        print(f"{'*'*30} Found Contact {'*'*30}")
        print(f"Name: {contacts[contactId]['name']}")
        print(f"Email: {contacts[contactId]['email']}")
        print(f"Phone: {contacts[contactId]['phone']}")
    else:
        print(f"Contact '{contactName}' not found.")


def updateContact(contacts, contactName):
    contactUpdated = False
    contactId = contactSearch(contacts, contactName)
    if contactId:
        print(f"{'*'*30} Found Contact {'*'*30}")
        print(f"{'*'*30} Current Details: {'*'*30}")
        print(f"(1) Name: {contacts[contactId]['name']}")
        print(f"(2) Email: {contacts[contactId]['email']}")
        print(f"(3) Phone: {contacts[contactId]['phone']}")
        print(f"{'*'*30} End of Details. {'*'*30}")
        attribNumber = int(input("Enter number of the attribute you want to change: "))
        newValue = input("New value for the attribute: ")
        if attribNumber == 1:
            contacts[contactId]['name'] = newValue
            contactUpdated = True
        elif attribNumber == 2:
            contacts[contactId]['email'] = newValue
            contactUpdated = True
        elif attribNumber == 3:
            contacts[contactId]['phone'] = newValue
            contactUpdated = True
        else:
            print("Invalid attribute.")
        if contactUpdated:
            print("Contact Updated.")
    else:
        print(f"Contact '{contactName}' not found.")
    return contacts


def deleteContact(contacts, contactName):
    contactRemoved = False
    contactId = contactSearch(contacts, contactName)
    if contactId:
        contacts.remove(contactId)
        contactRemoved = True
    if contactRemoved:
        print(f"Contact '{contactName}' was removed.")
    else:
        print(f"Contact '{contactName}' was not found.")
    return contacts


def writeContactsToFile(contactsFile):
    with open(contactsFile, 'w') as file:
        file.write(','.join(contacts[0].keys()))
        file.write('\n')
        for contact in contacts:
            file.write(','.join(contact.values()))
            file.write('\n')


contactsFile = 'contacts.csv'
contacts = getContactsFromFile(contactsFile)
requiresContactName = ['U', 'D', 'R']

print(f"{'*'*30} EasleyContact Pro v3.1.3.3.7 {'*'*30}")
while True:
    print("\nCommands: (C)reate a new contact (R)etrieve contact (U)pdate (D)elete -- (W)rite contact file (Q)uit")
    command = input("Enter command: ").upper()
    if command in requiresContactName:
        contactName = input("Enter contact name: ")

    if command == 'C':
        contacts = createContact(contacts)
    elif command == 'R':
        retrieveContact(contacts, contactName)
    elif command == 'U':
        contacts = updateContact(contacts, contactName)
    elif command == 'D':
        contacts = deleteContact(contacts, contactName)
    elif command == 'W':
        writeContactsToFile(contactsFile)
    elif command == 'Q':
        break
