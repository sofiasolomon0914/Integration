
# NOTES FROM PYTHON ACTIVITY 1: Print Statements

print("Go!")
# This is called a print statement, which means that when the code is run it will print Go!
# Print statements only work by the format print("whatever you want to print")
# Without the parenthesis it will give a syntax error

print("Hello.\nMy name is Pat")
# The .\n will cause the rest of the statement to continue on the next line

print("Age:", 20)
# The comma inside the print statement will create a space between both the age and 20
# The parenthesis in the print statement creates a string literal


# NOTES FROM PYTHON ACTIVITY 2: Input and Variables
name = input("What is your name? ")
print("Your name is", name)
# Both input() and print() are functions in python
# The input function will cause what is inside the paranthesis to be prompted when the code is ran
# What the user types into the prompt will then be stored in the variable name
# Variables cannot have special characters or numbers

# The following is another example
name = input("Enter your name: ")
ID = input("Enter your course name: ")
course = input("Enter your course number: ")
print(name + "'s ID is " + ID + "\nand is enrolled in " + course)


# NOTES FROM PYTHON ACTIVITY 3: Arithmetic Operations and Assignment Statements The following operates will be

# addition, subtraction, multiplication, to the power of, division, floor division, and modules (in that order)
print(16 + 3)
print(16 - 3)
print(16 * 3)
print(16 ** 3)
print(16 / 3)
print(16 // 3)
print(16 % 3)
# Keep in mind that you cannot add string or use operators with string statements An exception is multiplying a

# string, in that case it will just print the string statement the amount of times it was multiplied by(example below)
myWord = "Hello!" * 10
print(myWord)
# Even if variables are strings you can use the multiplication command and it will print the string literal the
# amount of times it was multiplied by

# The following program will prompt the user for two numbers and then it will subtract them
firstNumber = input("Enter a number: ")
secondNumber = input("Enter another number: ")
num1 = int(firstNumber)
num2 = int(secondNumber)
difference = num1 - num2
print("Difference = ", difference)
# The function int() turns a number into an integer
# This allows you to use commands with the number listed as a variable


# NOTES FROM PYTHON ACTIVITY 4: Formatting Output

# The following example will be shown twice, the first time being un-formatted
# and the second being formatted
numLaptops = 7
laptopCost = 599.50
price = numLaptops * laptopCost
# The following line will be un-formatted
print("Total cost of laptops", price)
# The following line will be formatted
# Notice that the formatted version will have a dollar sign, the correct amount of decimal
# points, and no space between the dollar sign and price
print("Total cost of laptops: $", format(price, '.2f'), sep='')

# The following code example calculates total cost of an item
# Getting information
itemName = input("Enter the name of the item: ")
numItems = int(input("Enter the number of items: "))
itemCost = float(input("Enter the cost of one item: "))
# Calculating price
totalCost = numItems * itemCost
# Printing results
print("Item name: ", itemName)
print("Cost of one item: ", itemCost)
print("Number of items purchased: ", numItems)
print("\nTotal cost: $", format(totalCost, "0.2f"), sep='')


# NOTES FROM PYTHON ACTIVITY 5: Boolean Expressions

# Meaning of each conditional operator are shown below
#  <  LESS THAN
#  >  MORE THAN
#  <= LESS THAN OR EQUAL TO
#  != NOT EQUAL TO
#  == EQUAL TO

# Examples using operators
x = 4
y = 5
z = 4
x > y
x < y
x == y
x != y
x >= z
x <= z x+ y > 2 * x
y * x - z != 4 % 4 + 16
pow(x, 2) == abs(-16)
# Using word will not work because they have to be integers,
# Using words will lead to a correct output

# To test more than one condition use a logic operator to create a compound condition
(age > 17) and (hasLicense == true)
# To be true the they must have a license and be at least 17
(cost < 20.00) or (shipping == 0.00)
# If the cost is greater than 20 then the shipping is free
not (credits > 120)
# There can be no more than 120 credits


# NOTES FROM PYTHON ACTIVITY 6: IF-ELSE Statements

# Below is an example of if-else being used to run a code
grade = 95
if grade >= 94:
    print("Excellent")
# This code says that if the grade submitted is greater than 94 then the output will be Excellent!
originalPrice = float(input("Enter the original cost of the item: "))
salePrice = float(input("Enter the sale price: "))
percentOff = int((originalPrice - salePrice) / originalPrice * 100)
print("Original price: $", format(originalPrice, ".2f"), sep="")
print("Sale price: $", format(salePrice, ".2f"), sep="")
print("Percent off: ", format(percentOff, "d"), "%", sep="")
if (percentOff >= 50):
    print("You got a great sale!")
# Float is used to return a floating point number from a number or a string

# Another example of using if-else
temperatureString = input("Enter the water temperature in degees Fahrenheit: ")
temperature = int(temperatureString)
if temperature >= 212:
    print("Water is boiling.")
else:
    print("The water is not boiling.")


# PYTHON ACTIVITY 7: Nested IF-ELSE Statements
# In python you can use elif instead of IF-ELSE Statement

# The following is a program example using elif
grade = int(input("Enter your grade: "))
if grade > 100 or grade < 0:
    print("Error")
elif grade >= 90:
    print("Very Good!")
elif 80 <= grade < 89:
    print("Good!")
elif 70 <= grade < 80:
    print("Satisfactory")
elif 60 <= grade < 70:
    print("Fair")
elif grade < 60:
    print("Poor")


# PYTHON ACTIVITY 8: Looping Structures(WHILE Loops)

# The following is an example of a while loop
name = input("Enter your name: ")
x = 0
while(x < 20):
    print(name)
    x = x + 1
# The statement above re-evaluates the value of x by adding 1 to x and then that being the new value and so on

# The following example will print the number entered and all preceding number down to 0
number = int(input("enter a number: "))
x = 1
while(x <= number):
    if(x%10 == 0):
        print(x)
    else:
        print(x, end=" ")
    x = x + 1


# PYTHON ACTIVITY 9: Looping Structures: FOR Loops

# The example below will show two programs that produce the same output, but one using a WHILE loop and the other using a FOR Loop
name = input("Enter your name: ")
x = 0
while(x < 20):
    print(name)
    x = x + 1
name = input("Enter your name: ")
for x in range(20):
    print(name)
# Notice that the FOR Loop is more concise

# The range function restricts the output to only the number included in the range
# The following will output [ 0 1 2 3 4 ]
for x in range(5):
    print(x, end=" ")

# The following will output [1 2 3 4]
for x in range(1,5):
    print(x, end=" ")

# The following will output [ 3 5 7 9 11 13 15 17 19 ]
for x in range(3,20,2):
    print(x, end=" ")

# The following will output [ 0 1 2 3 4 5 ]
numIterations = 6
for x in range(numIterations):
    print(x, end=" ")

# The following will output [ 1 2 3 4 5 6 ]
numIterations = 6
for x in range(1, numIterations+1):
    print(x, end=" ")

# The following code will list a flavor 4 times
favorite = input("Enter your favorite ice cream flavor: ")
for x in range(1,5):
    print(str(x) + ".", favorite, end="\t")
# Keep in mind that this program turns the integer into a string so that is can shown in the output

# The following program will prompt the user for 5 numbers and then add them all together
total = 0
for x in range(5):
    number = int(input("Enter a number: "))
    total += number
print("The total is:",total)


# PYTHON ACTIVITY 10: Looping Structures -- Nested Loops

# Refer to the following example for a nested loop
name = input("What is your name: ")
for x in range(5):
    for x in range(3):
        print(name + " ", end=" ")
    print()

# Create a code segment that prompts the user for a number between 1 and 10
# and then prints that many asterisks (*) on one line.
# Use a FOR loop. Although you should test the user input to be sure it is in range (between 1 & 10),
# you do not need to do that here.
numOne = int(input("Enter how many you would like in the x-axis: "))
numTwo = int(input("Enter how many you would like in the y-axis: "))
name = "*"
for x in range(numOne):
    for x in range(numTwo):
        print(name+" ", end=" ")
    print()

# Edit the program above so that it prints numbers instead of asterisks
height = int(input("Enter height: "))
column = int(input("Enter number of columns: "))
value = 1
for x in range(height):
    for x in range(column):
        print(value, end=" ")
    value += 1
    print()


# PYTHON ACTIVITY 11: PREDEFINED/BUILT-IN FUNCTIONS
print(abs(4.67))
print(pow(5,3))
print(pow(49,.5))
print(int(34.8))
print(round(6.9))
import random
print(random.randint(1,100))

abs(4.5)
int("678")
round(-5.6)
import random
random.randint(4,10)
# without running [import random] it will not have the random module to generate a random number

import math
x = 4.7
y = 5.3
z = -4.8
a = -3.2
print(math.ceil(x))
print(math.ceil(y))
print(math.ceil(z))
print(math.ceil(a))
print(math.floor(x))
print(math.floor(y))
print(math.floor(z))
print(math.floor(a))
# The ceil() function rounds up with positive numbers and rounds down with negative numbers
# The floor() function rounds down with positive numbers and rounds up with negative numbers
# They must be preceded by [math.] because they are a math modulet

# Following is an example program
doAgain = True
while doAgain:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    num4 = int(input("Enter fourth number: "))
    maxNum1 = max(num1, num2, num3, num4)
    print("The largest of the four numbers is: ", maxNum1)
    another = input("Type 'y' to find another max number " + "or any other key to quit")
    if another != 'y':
        doAgain = False
print("Done!")


# PYTHON ACTIVITY 12: Void Functions

# Description: This program uses a function to print a message
# Function definition
def printMessage():
    print("Welcome to Python.")
    print("Learn the power of functions!")
    # Function definition
def main():
    print("Hello Programmer!")
    # Function call
    printMessage()
# Function call
main()

# Description: This program uses functions to calculate
# the area of a circle, given the radius
import math
def calculateArea(radius):
    area = math.pi * radius ** 2
    print("Area of a circle with a radius of", radius, "is",
          format(area, ".2f"))
    diameter = radius * 2
    print("The diameter is ", diameter)
def main():
    radius = int(input("Enter the radius: "))
    calculateArea(radius)

##### Call to Main #####
main()


# ACTIVITY: VALUE RETURNING FUNCTIONS

import math
def getQuadratic(a,b):
    square = a**2 + b**2
    squareRoot = math.sqrt(square)
    return squareRoot
def main():
    print("The square root of the sum of the square of 3 and 4 is:", getQuadratic(3,4))

######### Call to main() ##########
main()