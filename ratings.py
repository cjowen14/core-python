"""Restaurant rating lister."""


# put your code here


#import txt file
dictionary = {}
with open("scores.txt") as scores:
    for line in scores:
        (key, val) = line.rstrip("\n").split(":")
        dictionary[key] = val

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

def main():
    #user input for what they would like to do
    user_choice = int(input("What would you like to do? (Enter the number)\n 1. See all ratings\n 2. Add a new restaurant\n 3. Quit\n"))
    if user_choice == 1:
        see_ratings()
    elif user_choice == 2:
        rest_name()
    elif user_choice== 3:
        print("Thank you for visiting!")
    else:
        print("Invalid Entry.")
        main()

main()




