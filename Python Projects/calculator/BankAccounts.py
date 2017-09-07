import math

#TODO: KEEP WORKING ON IT
#TODO: ADD A WAY TO READ INFO FROM FILE

exited = False

verified = False
balance = 0

name = str(input("Please create a username: "))
pswd = str(input("Please create a password: "))
def login():
    global verified
    if verified == False:

        loginName = str(input("Login: Enter username - "))
        loginPswd = str(input("Login: Enter password - "))
    if (loginName == name and loginPswd == pswd):
        verified = True
    else:
        print("Invalid login credentials!")
        login()
login()
def greet():
    print("Welcome to the Python Bank!")
    print("1) Check Balance")
    print("2) Perform a transaction")
    print("3) Exit")
    print("4) Help")

def transactions():
    transactionType = str(input("Withdraw (w) or Deposit (d)? "))
    transactionType.lower()
    global balance #omg this is so useful
    if (transactionType == "w" or transactionType == "withdraw"):
        if (balance <= 0):
            print("Error withdrawing! Negative balance!")
        wAmount = float(input("Enter withdrawal amount: "))
        print("Withdrawing... ")
        balance-=wAmount
        print("Withdrew " + str(wAmount) + "! Current balance: " + str(balance))

    if (transactionType == "d" or transactionType == "deposit"):
        dAmount = float(input("Enter deposit amount: "))
        print("Depositing... ")
        balance+=dAmount
        print("Deposited " + str(dAmount) + "! Current Balance: " + str(balance))

def checkBalance():
    print(balance)
if verified:
    greet()

def printCommands():
    print("1) Check Balance")
    print("2) Perform a transaction")
    print("3) Exit")
    print("4) Help")
    print("5) Logout")

while exited == False:

    #transactions()

    userCommand = str(input(">>> "))

    if (userCommand == "1"):
        checkBalance()

    if (userCommand == "2"):
        transactions()

    if (userCommand == "3"):
        print("Thank you for doing buisness with us, " + name + "!")

        f = open("bankInfo.txt", 'w')
        f.write("Balance: " + str(balance) + "\n" + "Username: " + name + "     ||     Password: " + pswd)
        f.close()

        exited = True
        exit()

    if (userCommand == "4"):
        printCommands()

    if (userCommand == "5"):
        print("Logging out... ")
        verified = False




