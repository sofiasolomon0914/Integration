# Sofia Solomon
# This program will help you calculate your semester GPA, it requires you to input the number of credits and the grade
# for each class. Enjoy!

totalCredits = int(input("How many credits are you taking this semester? "))
classOneCredit = int(input("How many credits is your first class? "))
classOneGrade = float(input("What is your grade in your first class? "))
classTwoCredit = int(input("How many credits is your second class? "))
classTwoGrade = float(input("What is your grade in your second class? "))
classThreeCredit = int(input("How many credits is your third class? "))
classThreeGrade = float(input("What is your grade in your third class? "))
classFourCredit = int(input("How many credits is your fourth class? "))
classFourGrade = float(input("What is your grade in your fourth class? "))
classFiveCredit = int(input("How many credits is your fifth class? "))
classFiveGrade = float(input("What is your grade in your fifth class? "))
quality_ptsOne = classOneCredit * classOneGrade
quality_ptsTwo = classTwoCredit * classTwoGrade
quality_ptsThree = classThreeCredit * classThreeGrade
quality_ptsFour = classFourCredit * classFourGrade
quality_ptsFive = classFiveCredit * classFiveGrade
quality_ptsTotal = quality_ptsOne + quality_ptsTwo + quality_ptsThree + quality_ptsFour + quality_ptsFive
semesterGPA = quality_ptsTotal / totalCredits
print("Your predicted semester GPA is {:.2f}".format(semesterGPA))



