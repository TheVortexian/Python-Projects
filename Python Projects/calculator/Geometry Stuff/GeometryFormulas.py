#Geometry equations
import math

def distance(x1, y1, x2, y2):
    distanceForm = math.sqrt((((x2-x1)**2)) + ((y2-y1)**2))
    print(distanceForm)

def midpoint(x1, y1, x2, y2):
    midpointX = ((x1 + x2) / 2)
    midpointY = ((y1 + y2) / 2)
    midpointResult = "(" + (str(midpointX)) + ", " + (str(midpointY)) + ")"
    print(midpointResult)

def pythagoreanTheorem():
    userChoice = str(input("Find a, b, or c: "))
    if (userChoice == "c"):
        a = float(input("Enter 'a': "))
        b = float(input("Enter 'b': "))
        findC = math.sqrt((a**2) + (b**2))
        print("Length: " + (str(findC)))
    if (userChoice == "b"):
        a = float(input("Enter 'a': "))
        c = float(input("Enter 'c': "))
        findB = math.sqrt((a**2) + (c**2))
        print("Length: " + str(findB))
    if (userChoice == "a"):
        c = float(input("Enter 'c': "))
        b = float(input("Enter 'b': "))
        findA = math.sqrt((b**2) + (c**2))
        print("Length: " + str(findA))

userExit = 0

while (userExit == 0):
    userCommand = str(input("Distance Formula, Midpoint Formula, Angle Formula, Pythagorean Theorem, [df] or [mf] or [pt] or exit: "))
    if (userCommand == "df"):
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        distance(x1, y1, x2, y2)

    if (userCommand == "mf"):
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        print(midpoint(x1, y1, x2, y2))

    if (userCommand == "pt"):
        pythagoreanTheorem()

    #TODO: MIDPOINT FORMULA

    if (userCommand == "exit"):
        exit()