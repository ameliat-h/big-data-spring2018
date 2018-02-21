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
#?? is there a way to add a period at the end of this too? most definitely, come back 2/18.
sentence_space = ' '
print(sentence_space.join(sentence_words))

#B.2: Reverse the order of this list using the .reverse() method, then print. Your output should begin with ["them", "visualize", ...].
# Reversing the order of the list:
sentence_words.reverse()
#print dat shit
print(sentence_words)


#B.3 Now use the .sort() method to sort the list using the default sort order.
sentence_words.sort()
#gonna print this now in prep for B.4
print(sentence_words)

#B.4 Perform the same operation using the sorted() function. Provide a brief description of how the sorted() function differs from the .sort() method.
sorted(sentence_words)
print(sentence_words)

#The printed outputs of both the sorted() function and the .sort() method are the same. I was a bit confused by the explanation contained on the course's github: https://github.com/ameliat-h/big-data-spring2018/blob/master/week-02/WS01_Python-Intro.md, so I looked it up and found the following at Quora: https://www.quora.com/What-is-the-difference-between-sort-and-sorted-function-in-Python :
# The difference is in how they operate on the list: .sort() modifies the list in place, whereas sorted() actually modifies the list and returns a new one. sorted() doesn't modify the original list.
# more info at python documentation here: https://docs.python.org/3/library/functions.html?highlight=sorted#sorted

#B.5 Extra Credit: Modify the sort to do a case-insensitive alphabetical sort.
# not sure if this means we are limited to using either .sort() or sorted()
sentence_words.sort(key=lambda s: s.lower())
print(sentence_words)

#C: Implement your own random function that builds on this python function, returning an integer between a low and a high number supplied by the user, but that can be called with the low number optional (default to 0).
#reference python function below (3lines)

from random import randint

def userinput():
        low = int(input("Please provide a low number "))
        if low < 0:
            low = 0
        high = int(input("Please provide a high number "))
        return randint(low, high)

assert(low <= userinput() <= high)
assert(50 <= userinput() <= 100)


#D: Write a function that expects two inputs. The first is a title that may be multiple words, the second is a number. Given these inputs, print the following string (replacing n and title with dynamic values passed to the script.)
# The number n bestseller today is: title
# Ask for the user to define the values of two variables, title and place
name = input('Enter the name of a book: ')
place = input('Enter a number between 1-10: ')

Proper_name = name.title()
#print using a f string to produce a dynamic string based on the input-generated values of the two variables (title and place)
msg = f"The number {place} bestseller today is: {Proper_name}."
print(msg)

#E. Write a function that evaluates the strength of a password. Ask the user to input a password that meets the criteria listed below. You can either use the Python input built-in function, or just pass the password as a function argument. Validate that the user’s password matches this criteria. If password is valid, print a helpful success message.
# the password has to be:
    # 8-14 characters long
    # includes at least 2 digits
    # includes at least 1 uppercase letter
    # includes at least one of the following special characters: ['!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']

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
chars = '!?@#$%^&*()-_+='
    ##ENDED HERE AND GOT RID OF BRACKETS ON CHARS

s = "It's not safe to go alone. Take this."
>>> 'safe' in s
True
>>> 'blah' in s
False
>>> if 'safe' in s:
...     print('The message is safe.')
The message is safe.


#if chars
#another approach: make chars string, and test to see if a string has any letters in common with pw list
if set.intersection is not none:
special_char = chars.count(pw) >= 1
print(special_char)
# Examples of string methods: .find(), which returns the index of the first instance of a substring and .count(), which returns the number of occurrences of a particular substring.
#string.find("Another")
#string.count("i")

# defining variable for has at least one special character
# def pw_special_char():

# if then statement to test
if pw_length and pw_num_digs and pw_upper and special_char:
    print("Niiiiice password.")
else:
    print("You didn't meet all criteria, try again.")



# pw.islower()
#     8 <= length <= 14
#     if char_count and digit and upper and :
#
#     else
#
#
# while x:
#     # is between 8-14 characters
#
#     if (len(pw)<8 or len(pw) > 14):
#         break
#     #has at least 2 digits
#     elif len([x.ifdigit() for x in pw]) >= 2:
#         break
#     #contains at least 1 uppercase letter
#     elif pw.isupper():
#         break
#     #contains at least 1 special character
#     elif not re.search("[0,!,?,@,#,$,%,^,&,*,(,),-,_,+,=]",pw):
#         break
#     else:
#         print("Nice strong password!")
#         x=False
#         break
#
# if x:
#     print("Try again, making sure all criteria are met!")

    #OTHER ATTEMPTS

# #now we'll test for these necessities using the 'while' loop or the if [statement] branch??
# print(8 <= len(password) <= 14)
# print( )

#F. Create a function called exp that accepts two integers and then return s an exponentiation, without using the exponentiation operator ( ** ). You may assume these are positive integers. Use at least one custom-defined function.

def exp():
    base =
    power =
    return #central concept of functions! return means create an object that is the yield
# when a function is done spit out something
# function doesn't do anything automatically to a return: to do something with the return, assign an object to it

    # use a loop
