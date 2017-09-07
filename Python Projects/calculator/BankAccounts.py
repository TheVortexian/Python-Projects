import math
import re

#TODO: KEEP WORKING ON IT
#TODO: ADD A WAY TO READ INFO FROM FILE?

exited = False

balance = 0
def checkIfHasAccount():
    pastUser = str(input("Please enter your account name: "))
    f = open("bankInfo.txt", 'r')
    for line in f:
        if pastUser in line:
            print("Welcome, " + pastUser + "!")

command1 = str(input("Have you used us before? y/n: "))
if command1 == "y":
    checkIfHasAccount()
if command1 == "n":
    print("Creating empty account. When you log out, enter an account name!")

def greet():
    print("Welcome to the Python Bank!")
    print("1) Check Balance")
    print("2) Perform a transaction")
    print("3) Exit")
    print("4) Help")
    print("5) Clear .txt File")

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

greet()

while exited == False:

    userCommand = str(input(">>>  "))

    if (userCommand == "1"):
        checkBalance()

    if (userCommand == "2"):
        transactions()

    if (userCommand == "3"):
        name = str(input("What is your account name? "))
        print("Thank you for doing buisness with us, " + name + "!")

        f = open("bankInfo.txt", 'a') #use 'a' for 'appending' instead of writing
        f.write("BANK INFORMATION: \n\nBalance: " + str(balance) + "\n" + "Account Name: " + name)
        f.close()

        exited = True
        exit()

    if (userCommand == "4"):
        greet()

    if (userCommand == "5"):
        f = open("bankInfo.txt", 'w')
        f.write("")
        f.close()



