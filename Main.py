

#Notes from python activity 1

print("Go!")
#This is called a print statement, which means that when the code is run it will print Go!
#Print statements only work by the format print("whatever yout want to print")
#Without the parathensis it will give a syntax error
print("Hello.\nMy name is Pat")
#The .\n will cause the rest of the statement to continue on the next line
print("Age:",20)
#The comma inside the print statement will create a space between both the age and 20
#The parenthesis in the print statement creates a string literal

#NOTES FROM PYTHON ACTIVITY 2: IF-ELSE Statements

grade = 95
if grade >= 94:
    print("Excellent")
#This code says that if the grade submitted is greater than 94 then the output will be Execellent!
originalPrice = float(input("Enter the original cost of the item: "))
salePrice = float(input("Enter the sale price: "))
percentOff = int((originalPrice - salePrice)/originalPrice * 100)
print("Original price: $", format(originalPrice, ".2f"), sep="")
print("Sale price: $", format(salePrice, ".2f"), sep="")
print("Percent off: ", format(percentOff, "d"),"%", sep="")
if(percentOff >= 50):
    print("You got a great sale!")