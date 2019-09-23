# NOTES FROM PYTHON ACTIVITY 1: Print Statements
print("Go!")
# This is called a print statement, which means that when the code is run it will print Go!
# Print statements only work by the format print("whatever yout want to print")
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
ID = input("Enter your name: ")
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



# NOTES FROM PYTHON ACTIVITY 6: IF-ELSE Statements

grade = 95
if grade >= 94:
    print("Excellent")
# This code says that if the grade submitted is greater than 94 then the output will be Execellent!
originalPrice = float(input("Enter the original cost of the item: "))
salePrice = float(input("Enter the sale price: "))
percentOff = int((originalPrice - salePrice) / originalPrice * 100)
print("Original price: $", format(originalPrice, ".2f"), sep="")
print("Sale price: $", format(salePrice, ".2f"), sep="")
print("Percent off: ", format(percentOff, "d"), "%", sep="")
if (percentOff >= 50):
    print("You got a great sale!")
