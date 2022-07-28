'''
List :-

'''
# list set tuple if else for def

string = "I love python"

#slicing   [start:end:steps = 1]
# start is always inclusive
# end is always exclusive

# print(string[2:6]) #love
# print(string[7:13]) #I


#reverse string using string slicing

# word = "Japan"
# print(word[::-1])
#love

# list1 = [1,23,45,65]

# print(list1[0]) #1
# print(list1[-1]) #65

# input_word = input("Enter the random word:-")
# print(input_word)

# reverse_word = input_word[::-1]
# # print(reverse_word)

# #Mam mM aA bB
# # = assignment operator      == comparaing
# if input_word == reverse_word:   
#     print("Given word is a palindrome")
# else:
#     print("Pls enter a valid word")

'''
if condition:
    print()
else:
    print()

'''


'''

List can have multiple datatype
List is a mutable data type  change/modify/edit
'''
list1 = [1,2,3,"Jack","Sam",True,False,["hello","bye","Java"],(11,22,33)]
# print(list1[1:4]) #2,3,jack
# print(list1[::])  # all data
# print(list1[::2])

# print(list1[7][2])


list1 = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', 'h',[[111,222,333],["India"]],["mumbai"],[["Python",245,658,44,10.0]]]

'''
bb
ddd
ee
h
[111,222,333]
333
["India"]
India
Mumbai
python
10.2
["Python",245,658,44,10.0]
'''

# print(list1[1][0])
# print(list1[1][1][1])
# print(list1[1][2])
# print(list1[3])
# print(list1[4][0])
# print(list1[4][0][2])
# print(list1[4][1])
# print(list1[4][1][0])
# print(list1[5][0])
# print(list1[6][0][0])
# print(list1[6][0][4])
# print(list1[6][0])


'''
Methods:-
1)Add element
2)change element
3)copy list
4)sorting

'''
# 1)Add element
fruits = ["apple","mango","banana","grapes"]
#append():- adding the value at the end of the list
# insert(index,value):- add the element at given index
print(fruits)
# fruits.append("watermelon")
# fruits.insert(4,"watermelon")
# print(fruits)


# 2)change element
fruits[3] = "pineapple"
print(fruits)


# 3)copy list

sample = fruits
print(sample)

# 4)sorting

num = [5,7,9,2,1,22,35]
print("before sorting:- ",num)
num.sort()
print("After sorting:-",num)


'''

append() :-  add the element at the end of the list


how can ['1','2','3'] be converted into [1,2,3]
op =[]
for i in lst1:
    x= int(i)
    op.append(x)

'''

'''
Method	                  Description
append()            Adds an element at the end of the list
clear()         	Removes all the elements from the list
copy()          	Returns a copy of the list
count()	            Returns the number of elements with the specified value
extend()            Add the elements of a list (or any iterable), to the end of the current list
index()         	Returns the index of the first element with the specified value
insert()            Adds an element at the specified position
pop()           	Removes the element at the specified position
remove()            Removes the item with the specified value
reverse()           Reverses the order of the list
sort()          	Sorts the list
'''
