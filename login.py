users = {}
status = ""
def displayMenu():
    status=input("Are you a registered user?[y/n]Press q to quit:")
    if status=="y":
        oldUser()
    elif status=="n":
        newUser()


def newUser():
    createLogin=input("Create login name:")
    if createLogin in users:
        print("\nLogin name already exists\n")
    else:
        createPW=input("Create password:")
        users[createLogin]=createPW
        print("\nUser created\n")


def oldUser():
    login=input("Enter login name:")
    PW=input("Enter password:")
    if login in users and users[login]==PW:
        print("\nLogin successful\n")
        import main
        print("=======================================================================================================================")
        main.MainMenu()
        ans=input("Would you like to return to the Main Menu? Press 'Y' to return or press 'X' to logout:")
        while ans.upper()=='Y':
            print("=======================================================================================================================")
            main.MainMenu()
            ans=input("Would you like to return to the Main Menu? Press 'Y' to return or press 'X' to logout:")
            if ans=="X":
                displayMenu()
    else:
        print("\nUser doesn't exist\n")
while status!="q":
    displayMenu()



    
    
