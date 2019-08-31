# This program checks for the character frequency in the given string.

def charFrequency(userInput):
    dict = {}
    for x in userInput:
        dict[x] = dict.get(x, 0) + 1
    for k,v in dict.items():
        print('{} occurred {} times'.format(k, v))

userInput = input('Enter a string : ')
charFrequency(userInput)

# R occurred 1 times
# a occurred 3 times
# m occurred 1 times
# n occurred 1 times
# t occurred 1 times
# h occurred 1 times