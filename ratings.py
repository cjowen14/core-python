"""Restaurant rating lister."""


# put your code here

#function to ensure rating is between 1-5
def user_input():
    new_rat = input("What is the rating for the restaurant?\n")
    if float(new_rat) <=5 and float(new_rat) >=1:
        dictionary[new_rest] = new_rat
    else:
        print("Rating must be between 1-5.")
        user_input()

#import txt file
dictionary = {}
with open("scores.txt") as scores:
    for line in scores:
        (key, val) = line.rstrip("\n").split(":")
        dictionary[key] = val

#get user input for restaurant name and rating
new_rest = input("What is the name of the new restaurant?\n")
user_input()

#create a list with the dictionary items
list = dictionary.items()

#sort the new list
sorted_list = sorted(list)

#loop through the list to print name and rating in alphabetical order by restaurant
for i in sorted_list:
    print(i[0], "is rated at", i[1])