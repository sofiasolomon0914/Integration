# Sofia Solomon
# This program will help people use their free time more effectively by asking what they have done and
# what they feel like doing to generate suggestions of what they can do in their free time.

print("\nHello! I will ask you some questions to help you figure out what you should be doing right now. \nPlease keep in mind that this program is case sensitive and that you should answer each question in lowercase letters. ")


activity_homework = str(input("\nHave you completed all of your homework assignments? "))
tier_homework = True
while tier_homework:
    if activity_homework == "no":
        print("Go do your homework!")
        tier_homework = False
    elif activity_homework == "yes":
        print("Good job!")
        activity_exercise = str(input("Have you gone running yet today? "))
        tier_homework = False

tier_exercise = True
while tier_exercise:
    if activity_exercise == "no":
        print("Go running!")
        tier_exercise = False
    elif activity_exercise == "yes":
        print("good job!")
        activity_organize = str(input("Do you have everything organized? "))
        tier_exercise = False

tier_organize = True
while tier_organize:
    if activity_organize == "no":
        print("Go organize your life! This includes: room, car, papers, files, closet, etc.")
        tier_organize = False
    elif activity_organize == "yes":
        print("Yay! You have your most important activities completed and up to date, \nnow lets move onto the the "
              "next group of activities!")
        tier_organize = False





