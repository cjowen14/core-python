import random, os, sys

"""Restaurant rating lister."""


# put your code here

dictionary = {}
#import txt file
def open_dictionary(file_input):
    with open(file_input) as scores:
        for line in scores:
            (key, val) = line.rstrip("\n").split(":")
            dictionary[key] = val
    main(file_input)

#get new restaurant name        
def rest_name():
    new_rest = input("What is the name of the new restaurant?\n")
    rating_input(new_rest)

#get new restaurant rating and ensure its between 1-5
def rating_input(new_rest):
    new_rat = input("What is the rating for the restaurant?\n")
    if float(new_rat) <=5 and float(new_rat) >=1:
        dictionary[new_rest] = new_rat
        see_ratings()
    else:
        print("Rating must be between 1-5.")
        rating_input(new_rest)

#see ratings of current restaurants
def see_ratings():
    #create a list with the dictionary items
    list = dictionary.items()
    #sort the new list
    sorted_list = sorted(list)
    #loop through the list to print name and rating in alphabetical order by restaurant
    for i in sorted_list:
        print(i[0], "is rated at", i[1])
    print("\n")
    main()

#provide user with a random restaurant and let them change the rating
def change_random():
    list = dictionary.items()
    sorted_list = sorted(list)
    random_choice = random.choice(sorted_list)
    print("Your restaurant is", random_choice[0], "which has a current rating of", random_choice[1])
    new_rating = input("What would you like to change the rating to?\n")
    dictionary[random_choice[0]] = new_rating;
    main()

#allow user to select a restaurant to change the rating
def change_selected():
    list = dictionary.items()
    sorted_list = sorted(list)
    for i in sorted_list:
        print(i[0], "is rated at", i[1])
    user_choice = input("Please type the name of the restaurant you would like to update:\n")
    print("You have selected", user_choice)
    new_rating = input("What would you like to change the rating to?\n")
    for x in dictionary:
        if x == user_choice:
            dictionary[x] = new_rating
    print("Rating for", user_choice, "has been updated!")
    main()

#user input for what they would like to do
def main(file_input):
    user_choice = int(input("What would you like to do? You are currently in " + file_input + " (Enter the number)\n 1. See all ratings\n 2. Add a new restaurant\n 3. Change Random Rating\n 4. Choose a restaurant to update a rating\n 5. Choose another txt file\n 6. Quit\n"))
    if user_choice == 1:
        see_ratings()
    elif user_choice == 2:
        rest_name()
    elif user_choice == 3:
        change_random()
    elif user_choice == 4:
        change_selected()
    elif user_choice == 5:
        file_choice()
    elif user_choice == 6:
        print("Thank you for visiting!")
    else:
        print("Invalid Entry.")
        main()

def file_choice():
    dirs = os.listdir()
    print("List of current files:")
    for i in dirs:
        if not i == '.git' and not i == 'ratings.py':
            print(i)
    file_input = input("Which file would you like to access?\n")
    isFile = os.path.isfile(file_input)
    if isFile:
        dictionary.clear()
        open_dictionary(file_input)
    else:
        print("Must enter an exsisting file.")
        file_choice()
  
file_choice()