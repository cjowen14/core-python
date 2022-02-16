"""Restaurant rating lister."""


# put your code here

dictionary = {}
with open("scores.txt") as scores:
    for line in scores:
        (key, val) = line.rstrip("\n").split(":")
        dictionary[key] = val

new_rest = input("What is the name of the new restaurant?\n")
new_rat = input("What is the rating for the restaurant?\n")
dictionary[new_rest] = new_rat
list = dictionary.items()

sorted_list = sorted(list)

for i in sorted_list:
    print(i[0], "is rated at", i[1])
