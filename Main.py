
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
