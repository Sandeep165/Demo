def count_all(string):
    ltr, dgt = 0,0
    for i in string:
        if i.isalpha():
            ltr = ltr +1
        elif i.isdigit():
            dgt = dgt+1
    dict1 = {"LETTERS": ltr, "DIGITS": dgt}
    print(dict1)

# count_all("Hello World")


def is_symmetrical(numb):
    result = str(numb)
    if result == result[::-1]:
        print(True)
    else:
        print(False)

# is_symmetrical(121)
# is_symmetrical(100)


def filter_list(lst):
   
    output = []
    for i in lst:
        if str(i).isdigit():
            output.append(i)
        # print(output)
    print(output)

filter_list([1, 2, 3, "a", "b", 4])


'''
Create a function that takes a string and returns the number (count) of vowels contained within it.

Examples
count_vowels("Celebration") ➞ 5

count_vowels("Palm") ➞ 1

count_vowels("Prediction") ➞ 4
# i in "aeiou"

Lists can be mixed with various types. Your task for this challenge is to sum all the number elements in the given list.
Create a function that takes a list and returns the sum of all numbers in the list.

Examples
numbers_sum([1, 2, "13", "4", "645"]) ➞ 3

numbers_sum([True, False, "123", "75"]) ➞ 0

numbers_sum([1, 2, 3, 4, 5, True]) ➞ 15

data type addition

2 + "2"
'''
def numbers_sum(lst):
    sum1 =0
    for i in lst:
        if type(i) == int:
            sum1 = sum1+i
    print(sum1)
numbers_sum([1, 2, "13", "4", "645"])

'''
Q1:-
Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns
 a dictionary of objects like { "name": "John", "top_note": 5 }.

Examples
top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }

top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }

top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }

    dict1 = {"LETTERS": ltr, "DIGITS": dgt}
Q2:-

In BlackJack, cards are counted with -1, 0, 1 values:

2, 3, 4, 5, 6 are counted as +1
7, 8, 9 are counted as 0
10, J, Q, K, A are counted as -1
Create a function that counts the number and returns it from the list of cards provided.

Examples
count([5, 9, 10, 3, "J", "A", 4, 8, 5]) ➞ 1

count(["A", "A", "K", "Q", "Q", "J"]) ➞ -6

count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]) ➞ 5
sum[lst]
Q3:-
Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.

Examples
equal(3, 4, 3) ➞ 2

equal(1, 1, 1) ➞ 3

equal(3, 4, 1) ➞ 0 
Notes
Your function must return 0, 2 or 3.

Q4:
Create a function that takes a string as an argument and returns a coded (h4ck3r 5p34k) version of the string.

Examples
hacker_speak("javascript is cool") ➞ "j4v45cr1pt 15 c00l"

hacker_speak("programming is fun") ➞ "pr0gr4mm1ng 15 fun"

hacker_speak("become a coder") ➞ "b3c0m3 4 c0d3r"
Notes
In order to work properly, 
the function should replace all "a"s with 4, "e"s with 3, "i"s with 1, "o"s with 0, and "s"s with 5.



'''

string = "i love java"
print(string.replace("java","100"))
