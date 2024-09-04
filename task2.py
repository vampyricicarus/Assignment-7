# task 1

firstName = input("What is your first name? ")
lastName = input("What is your last name? ")

def name():
    if len(firstName) and len(lastName) >= 2:
        print("Welcome " + firstName + " " + lastName + "!")
    else:
        print("Invalid Name")
    return
name()
              