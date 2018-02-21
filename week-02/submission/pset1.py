#A.1 create a list containing any 4 strings
#forked poem from William Carlos Williams
l_poem = ['This', 'Is', 'Just', 'to Say']

#A.2 printing the third item in the lists
#remember to start from zero...
print(l_poem[2])

#A.3 printing the 1st and 2nd items in the list using [:] index slicing
#remember that this method stops short of the second number
print(l_poem[0:2])

#A.4 add a new string with text "last" to the end of the list and print the list (new list = l_poem2)
l_poem2 = ['last']
l_poem3 = l_poem + l_poem2

print(l_poem3)

#A.5 Get the list length and print it.
print(len(l_poem3))

#A.6 Replace the last item in the list with the string 'new' and print.
#replace last item (we know there are 5 items total from the list length command, so that's the 4th in python's count)
l_poem3[4] = 'new'
print(l_poem3)

#B Convert the following list...
sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']

#B.1 ...into a normal sentence with join(), then print.
# each string is one word, so we want to insert a space b/w each string to form a normal sentence.

space = " "
print(space.join(sentence_words))

#B.2: Reverse the order of this list using the .reverse() method, then print. Your output should begin with ["them", "visualize", ...].
# Reversing the order of the list:
sentence_words.reverse()
print(sentence_words)


#B.3 Now use the .sort() method to sort the list using the default sort order.
sentence_words.sort()
#gonna print this now in prep for B.4
print(sentence_words)

#B.4 Perform the same operation using the sorted() function. Provide a brief description of how the sorted() function differs from the .sort() method.
sorted(sentence_words)
print(sentence_words)

#The printed outputs of both the sorted() function and the .sort() method are the same. I was a bit confused by the explanation contained on the course's github: https://github.com/ameliat-h/big-data-spring2018/blob/master/week-02/WS01_Python-Intro.md, so I looked it up and found the following at Quora: https://www.quora.com/What-is-the-difference-between-sort-and-sorted-function-in-Python :
# The difference is in how they operate on the list: .sort() modifies the original list in place, whereas sorted() returns a new list. sorted() doesn't modify the original list.
# more info at python documentation here: https://docs.python.org/3/library/functions.html?highlight=sorted#sorted

#B.5 Extra Credit: Modify the sort to do a case-insensitive alphabetical sort.
# not sure if this means we are limited to using either .sort() or sorted()
sentence_words.sort(key=lambda s: s.lower())
print(sentence_words)

#C: Implement your own random function that builds on this python function, returning an integer between a low and a high number supplied by the user, but that can be called with the low number optional (default to 0).
#reference python function below (3lines)

from random import randint
def random_number(a,b=0):
    return randint(b,a)

assert(0 <= random_number(75) <= 75)
assert(51 <= random_number(75, b = 51) <= 100)

#D: Write a function that expects two inputs. The first is a title that may be multiple words, the second is a number. Given these inputs, print the following string (replacing n and title with dynamic values passed to the script.)
# The number n bestseller today is: title
# Ask for the user to define the values of two variables, title and place
name = input('Enter the name of a book: ')
place = input('Enter a number between 1-10: ')

Proper_name = name.title()
#print using a f string to produce a dynamic string based on the input-generated values of the two variables (title and place)
msg = f"The number {place} bestseller today is: {Proper_name}."
print(msg)

#E. Write a function that evaluates the strength of a password (criteria on pset handout)....
#ok! so, start with asking for user input, and then running a bunch of boolean tests on that input to see if they meet the criteria. If any one criterion isn't met, the password is denied...
#use break for whenever something is false
#sources of code snippets: #https://www.w3resource.com/python-exercises/python-basic-exercise-128.php
# and https://www.w3resource.com/python-exercises/python-conditional-exercise-15.php

import re

pw = (input("Enter a password that meets the following criteria: is 8-14 characters long; has at least 2 digits; has at least 1 uppercase letter; and has at least one of the following special characters: !, ?, @, #, $, %, ^, &, *, (, ), -, _, +, ="))

# defining variable for password length
pw_length = (8 <= len(pw) <= 14)
print(pw_length)
# defining variable for has at least 2 digits
pw_num_digs = sum([x.isdigit() for x in pw]) >= 2
print(pw_num_digs)
#defining variable for has at least one uppercase letter
pw_upper = sum([x.isupper() for x in pw]) >= 1
print(pw_upper)

# creating list for different special characters
spec_char = ['!','?','@','#','$','%','^','&','*','(',')','-','_','+','=']
#run loop on that list in the pw input
empty = []
for x in pw:
    if x in spec_char:
        empty.append(x)
print(empty)

# if then statement to test
if pw_length and pw_num_digs and pw_upper and empty:
    print("Niiiiice password.")
else:
    print("You didn't meet all criteria, try again.")

#F. Create a function called exp that accepts two integers and then |return|s an exponentiation, without using the exponentiation operator ( ** ). You may assume these are positive integers. Use at least one custom-defined function.

# use a for loop! special thanks to this topic: https://stackoverflow.com/questions/26248262/in-python-use-a-for-loop-and-multiplication-to-create-a-power-function

def power(base,exp):
  res = 1
  for _ in range(exp):
    res *= base
  return res
print(power(5,3))

#G: Write your own versions of the Python built-in functions min() and max(). They should take a list as an argument and return the minimum or maximum element. Assume lists contain numeric items only.

def power(base,exp):
  res = 1
  for _ in range(exp):
    res *= base
  return res
print(power(5,3))
