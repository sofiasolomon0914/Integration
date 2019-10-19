# Sofia Solomon
# This program will help people use their free time more effectively by asking what they have done and
# what they feel like doing to generate suggestions of what they can do in their free time.

print("\nHello! I will ask you some questions to help you figure out what you should be doing right now. \nPlease "
      "keep in mind that this program is case sensitive and that you should answer each question in lowercase "
      "letters. ")

# The following activities are part of the first section or tier of activities
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

# The following activities are part of the second tier of activities.

activity_study = str(input("\nDo you feel prepared for all of your exams and quizzes for the next week? "))
tier_study = True
while tier_study:
    if activity_study == "no":
        print("Go study for your exams and classes until you feel prepared.")
        tier_study = False
    if activity_study == "yes":
        print("Good job!")
        activity_music = str(input("Have you practiced all of your music for orchestra? "))
        tier_study = False

tier_music = True
while tier_music:
    if activity_music == "no":
        print("Go and practice. Make sure to practice for rehearsals and auditions!")
        tier_music = False
    if activity_music == "yes":
        print("Good job!")
        activity_socialMedia = str(input("Have you answered all of your emails, text messages and calls? "))
        tier_music = False
print("Congratulations!!! You have finished all of your activities! Now it is time to figure out what activity you "
      "will enjoy the most with your free time!")

# The following section with suggest the user activities based on their mood

userMood = str(input("\nHow are you feeling? Please choose between the following: tired, hyper, nervous, tense, upset, "
                     "depressed, calm. "))

moodLoop = True
while moodLoop:
    if userMood == "tired":
        print("\nMaybe try taking a nap. Or if you are tired but can't fall asleep try doing something relaxing but "
              "engaging, like reading or writing.")
        moodLoop = False
    if userMood == "hyper":
        print("\nGo out and have some fun!! See if there is a party or event you can go to! Just remember to  be "
              "careful, partying is fun, but not when you overdue it...")
        moodLoop = False
    if userMood == "nervous":
        print("\nOh no! Try taking some deep breaths. Then try to figure out what is making you nervous and see if "
              "you can find a solution to the problem. Try writing down and brainstorming solutions. If you are "
              "worrying to much about he future, remember, you cannot control the future. Do your best in the "
              "present and your future will work itself out.")
        moodLoop = False






