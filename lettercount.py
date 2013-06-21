
"""
Problem Description
-------------------
Write a program, lettercount.py, that opens a file named on 
the command line and counts how many times each letter occurs 
in that file. Your program should then print those counts to 
the screen, in alphabetical order. For example:

    inputfile.txt:
    An abacus

    $ python lettercount.py inputfile.txt
    3
    1
    1
    0
    0
    ...

We have provided a file 'twain.txt' for you to test your code on.
"""

from sys import argv

script, filename = argv

f = open(filename)
twain = f.read()

# initialize dictionary
count = {}

# The if statment checks if a char is an alphabetical letter
# the elif statement checks the alpha letter and makes them all lowercase
for char in twain:
    if char.isalpha() == False:
        continue # ignore non-alpha characters
    elif ord(char) < 91:
        char = char.lower()
    count[char] = count.get(char, 0) + 1


# This for loop goes through twain checking for all lowercas eletters (ie. range 97, 123)
# After checking in for loop it print thes number of times each letter appears in the document

for num in range(97, 123):
    letter = chr(num)
    print count.get(letter, 0)

f.close()

