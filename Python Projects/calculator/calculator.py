# Calculator with a lot of functions.

"""IMPORT STATEMENTS"""
import turtle
import re
import math
from math import sqrt
from math import factorial
from decimal import Decimal, getcontext

getcontext().prec = 100 #for PI algorithm

#GEOMETRY STUFF!
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

#Credit Card Checksum validator. Uses Luhn algorithm: https://en.wikipedia.org/wiki/Luhn_algorithm
def validate():
    'Validates any credit card number using LUHN method'

    number = str(input("Enter card number without spaces: "))
    re.sub(r' ', '', number)
    count = 0
    for i in range(len(number)):
        val = int(number[-(i+1)])
        if i % 2 == 0:
            count += val
        else:
            count += int(str(2 * val)[0])
            if val > 5:
                count += int(str(2 * val)[1])
    if count % 10 == 0:
        print("\nCard is valid!\n")
    else:
        print("\nCard is invalid.\n")

#Declare turtle graphics window, color, and points
def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

#Get midpoint
def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)
#Actually draw the triangle
def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
#display it
def draw():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-300,-150],[0,250],[300,-150]]
   sierpinski(myPoints,6,myTurtle)
   myWin.exitonclick()

#find pi to N decimal places
def findPi(n):
    t = Decimal(0)
    pi = Decimal(0)
    deno = Decimal(0)
    k = 0
    for k in range(n):
        t = ((-1) ** k) * (factorial(6 * k)) * (13591409 + 545140134 * k)
        deno = factorial(3 * k) * (factorial(k) ** 3) * (640320 ** (3 * k))
        pi += Decimal(t) / Decimal(deno)
    pi = pi * Decimal(12) / Decimal(640320 ** Decimal(1.5))
    pi = 1 / pi
    return print(pi)

#No 'power' function, easier to just do print(1**2)

#add
def add(x, y):
    sum = x + y
    print(sum)

#subtract
def subtract(x, y):
    answer = x - y
    print(answer)

#multiply
def multiply(x, y):
    answer = x * y
    print(answer)

#divide
def divide(x, y):
    quotient = x / y
    print(quotient)

#square root
def sqrt(number):
    answer = math.sqrt(number)
    print(answer)

#Sieve of Eratosthenes from 1 to N
def get_primes(n):
    m = n + 1
    numbers = [True for i in range(m)]
    for i in range(2, int(math.sqrt(n))):
        if numbers[i]:
            for j in range(i * i, m, i):
                numbers[j] = False
    primes = []
    for i in range(2, m):
        if numbers[i]:
            primes.append(i)
    return primes

#Convert number from decimal to binary
def toBinary():
    usernum = int(input("Enter the number in decimal form: "))
    print("{0:b}".format(usernum))

#Convert number from binary to decimal
def toDecimal():
    binary = input("Enter the binary code to convert: ")
    decimalAnswer = int(binary, 2)
    print(decimalAnswer)


userHasNotExited = True
while userHasNotExited:
    userChoice = input("\n[ccv] Credit Card Validation, [A]dd, [s]ubtract, [m]ultiply, [d]ivide, power[e], square root[sqrt], [p]rimes,\n[f]ind PI, [t]riangle, [tb] to binary, [td] to decimal,\n[pt] Pythagorean Theorem, [df] Distance Formula, [mf] Midpoint Formula, exit: ")
    if (userChoice == "add" or userChoice == "A" or userChoice == "a"):
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))
        add(num1, num2)

    if (userChoice == "subtract" or userChoice == "s"):
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))
        subtract(num1, num2)

    if (userChoice == "multiply" or userChoice == "m"):
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))
        multiply(num1, num2)

    if (userChoice == "divide" or userChoice == "d"):
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
        divide(num1, num2)

    if (userChoice == "power" or userChoice == "e"):
        baseNum = float(input("Enter base: "))
        power = float(input("Enter power: "))
        print(baseNum**power)

    if (userChoice == "square root" or userChoice == "sqrt"):
        num1 = float(input("Enter number to find the square root of: "))
        sqrt(num1)

    if (userChoice == "primes" or userChoice == "p"):
        limit = int(input("Enter upper limit: "))
        print(get_primes(limit))

    if (userChoice == "find PI" or userChoice == "f"):
        findPi(80)  # n = 80 is pretty much as far as the PI goes.
        # todo: improve PI algorithm

    if (userChoice == "triangle" or userChoice == "t"):
        draw()

    if (userChoice == "to binary" or userChoice == "tb"):
        toBinary()

    if (userChoice == "to decimal" or userChoice == "td"):
        toDecimal()
    if (userChoice == "Credit Card Validation" or userChoice == "ccv"):
        validate()

    if (userChoice == "mf"):
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        print("Midpoint: " + str(midpoint(x1, y1, x2, y2)))

    if (userChoice == "df"):
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        print(distance(x1, y1, x2, y2))

    if (userChoice == "pt"):
        pythagoreanTheorem()

    if (userChoice == "exit"):
        userhasNotExited = False
        exit()