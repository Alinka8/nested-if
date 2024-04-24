# task 1 part 1: Buggy code

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
if venue == "large hall":
    print("We will provide the hall with audio system and projector")
elif venue == "conference room":
    print("We will provide only the conference with audio system")
attendees = input("Would you like a vegetarian food? yes/no ")
food = "We have an option of Veggie Delight Caterers" if attendees == "yes" else "We have an option of Gourmet Meals Caterers"
print(food)