place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
     action = input("light a torch or proceed in the dark?")
     if action == "light a torch":
         print("You found a diamond")
     else:
        print("You found the bats")
else:
    pass
    print("invalid choice")