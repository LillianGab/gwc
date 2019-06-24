start = '''
Bobby is an alien who is lost on Earth. Help him get back to his spaceship and return home.
'''

keepplaying = "yes"
print(start)
while keepplaying == "yes" or keepplaying == "Yes":
    userChoice = input("What direction should Bobby go? Type left to go left. Type right to go right")
    if userChoice == "left":
        print("He walks in the left-hand direction and comes across a civilian. ")
        print("Now you must decide how Bobby should greet the civilian. ")
        print("")
        keepplaying = "no"
    elif userChoice == "right":
        print("He walks in the right-hand direction and comes across a mountain range")
        print("He spends days climbing the mountains and on the other side, he finds his spaceship and returns home! ")
        print("You have succeeded! ")
        keepplaying = input("Would you like to play again? Type yes or no. ")
        if keepplaying == "no":
            quit()
    else:
        print("Please select one of the valid options: left or right. ")
        keepplaying = input("Would you like to try again? Type yes or no. ")
        if keepplaying == "no":
            quit()

keepplaying = "yes"
while keepplaying == "Yes" or keepplaying == "yes":
    userChoice = input("Should Bobby nicely ask the civilian for help or push the civilian and run in the opposite direction? Type ask to ask for help and type run to run away. ")
    if userChoice == "ask":
        print("Bobby asks the civilian if they have seen a UFO around the city.")
        print("The civilian replies that there have been reported sightings around the mountain ranges beyond the city limits. ")
        print("Now you must decide whether Bobby should trust the civilian. ")
        print("")
        keepplaying == "no"
    elif userChoice == "run":
        print("Bobby violently pushes over the civilian and runs towards the mountain range on the left. ")
        print("However, before he is able to reach his destination, police officers who the civilian called after being pushed by Bobby capture him and he is sent to Area 51 for cruel experimentation. ")
        print("")
        keepplaying = input("You have failed your task because Bobby cannot return home. Would you like to try again? Type yes or no. ")
         if keepplaying == "no":
            quit()
    else:
        print("Please select one of the valid options: ask or run. ")
        keepplaying = input("Would you like to try again? Type yes or no. ")
        if keepplaying == "no":
            quit()

keepplaying = "yes"
while keepplaying == "Yes" or keepplaying == "yes":
    UserChoice input("Should Bobby trust the civilian and go towards the mountains? ")