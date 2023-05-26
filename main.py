print('"Batman!"')
print('"The Joker is hiding somehwere in the Batcave!"')
print('"What are we going to do!"')
print("Do you enter the Batcave?")

caveChoice = input("").lower()

if caveChoice == "yes":
    print("The cave opens")
    print("Where do you look first...?")
    print("A. The Batcomputer?")
    print("B. The Batmoile?")
    print("C. The shadows?")

    checkChoice = input("").lower()

    if checkChoice == "a" or checkChoice == "the batcomputer":
        print("Nothing here...")
        print("Want to take a closer look?")
        
        aChoice = input("").lower()

        if aChoice == "yes":
            print("Yup! Definitely nothing here...")
        elif aChoice == "no":
            print("Ok ... let's just call it a day")
        else:
            print("Please enter yes or no")

    elif checkChoice == "b" or checkChoice == "the batmobile":
        print("He's here!")
        print("You got him!")
    elif checkChoice == "c" or checkChoice == "the shadows":
        print("You fall into a hole and can't get out.")
        print("GAME OVER!!!")
    else:
        print("Please enter A or B or C")

elif caveChoice == "no":
    print("You go to bed, its Alfreds problem now.")
else:
    print("Please enter yes or no")

print("Thanks for Playing")