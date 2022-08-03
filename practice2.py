'''
#Conditional statement:- range

Q8. Write a program to calculate the electricity bill (accept number of unit from user) 
according to the following criteria :
             Unit                                                     Price  
First 100 units  (0-100)                                             no charge
Next 100 units    (101-200)                                          Rs 5 per unit
After 200 units  unit>200                                           Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)

210  =  0+100*5+10*10 = 500+100 = 600
                                      
Q9. Write a program to display the last digit of a number.
(hint : any number % 10 will return the last digit)

Q10. Write a program to check whether the last digit of a number( entered by user ) is 
divisible by 3 or not. 123 331

if elif else
fact = 1

fact*i
multiplication equation = 1
'''
from sys import stdin


def cal(unit):
    amount = 0
    if unit<100:
        print("No charge")
    elif unit>100 and unit<=200:
        amount = (unit-100)*5
        print("Amount need to pay is:- ",amount)
    else: #210
        amount = 500 + (unit-200)*10 #
        print("Amount need to pay is:- ",amount)

# cal(254)
# cal(310)
# cal(310)
# cal(159)

'''
 Write a program to accept percentage from the user and display the grade according to the following criteria:

         Marks                                    Grade
         > 90                                         A
         > 80 and <= 90                              B
         >= 60 and <= 80                             C
         below 60                                    D
'''


def result(marks):
    if (marks>90) :
        print("A")
    elif marks>80 and marks<=90:
        print("B")
    elif marks>=60 and marks<=80:
        print("C")
    else:
        print("D")
# result(90)
# result(44)
# result(88)
# result(88)
# result(60)

def result(marks):
    if marks<60:
        print("GRADE D")
    elif marks>=60 and marks<=80:
        print("GRADE C")
    elif marks>80 and marks<=90:
        print("GRADE B")
    elif marks>90:
        print("GRADE A")

# result(90)
# result(44)
# result(88)

'''
Create a function that takes a list of numbers lst and returns an inverted list.
loops
Examples
invert_list([1, 2, 3, 4, 5]) ➞ [-1, -2, -3, -4, -5]

invert_list([1, -2, 3, -4, 5]) ➞ [-1, 2, -3, 4, -5]

invert_list([]) ➞ []


'''
# lst = [1, -2, 3, -4, 5]
# for i in lst:
#     print(i)

def invert_list(ans):
    for i in ans:
        print(i*(-1))
        
# invert_list([1,2,3,4,-5])

lst = ["apple","mango","banana","cherry"]
output = []
output = ["apple","mango","banana"]
#in

# name = "Sandeep"
# if "x" in name:
#     print(True)
# else:
#     print(False)
# lst1 = []
# for i in lst:
#     if "a" in i :
#         lst1.append(i)

# print(lst1)

# [expression for items in iterable if condition == True]
result = [i for i in lst if "a" in i]
print(result)

lst = [1,2,3,4,5,6,7,8,9,10]
evn =[]
odd = []
# result = [6,7,8,9,10]
evn = [i for i in lst if i%2 ==0]
odd = [i for i in lst if i%2 ==1]
print(evn)
print(odd)




'''
Practice 
Q1:- 
Create a function that takes a list of strings and integers, and filters out the list so that it returns a list 
of integers only.

Examples
filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]

filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]

filter_list(["Nothing", "here"]) ➞ []

Q2:-
Create a function that takes a number as an argument and returns True or False depending on whether the number is
 symmetrical or not. A number is symmetrical when it is the same as its reverse.

Examples
is_symmetrical(7227) ➞ True

is_symmetrical(12567) ➞ False

is_symmetrical(44444444) ➞ True

is_symmetrical(9939) ➞ False

is_symmetrical(1112111) ➞ True

Q3:
Write a function that takes a string and calculates the number of letters and digits within it. 
Return the result in a dictionary.

Examples
count_all("Hello World") ➞ { "LETTERS":  10, "DIGITS": 0 }

count_all("H3ll0 Wor1d") ➞ { "LETTERS":  7, "DIGITS": 3 }

count_all("149990") ➞ { "LETTERS": 0, "DIGITS": 6 }

print({ "LETTERS": ltr, "DIGITS": dgt })
'''