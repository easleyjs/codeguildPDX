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


def createContact(contacts):
    contactName = input("Contact Name: ")
    contactEmail = input("Contact Email: ")
    contactPhone = input("Contact Phone: ")
    contacts.append(dict('name'=contactName, 'email'=contactEmail, 'phone'=contactPhone))
    return contacts


def removeContact(contacts, contactName):
    pass


def updateContact(contacts, contactName):
    pass


def deleteContact(contacts, contactName):
    pass


def writeContactsToFile(contactsFile):
    with open(contactsFile, 'r') as file:
        pass


contacts = getContactsFromFile('contacts.csv')

print(contacts)
