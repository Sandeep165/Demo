'''
Tuples :- ()

can stored multiple data type
immutable

count() :- count the occurence
index() :-  index of the value
'''

my_tuple = (1,2,3,"apple","apple","apple","apple","mango")
print(my_tuple.count("apple"))

i = my_tuple.index("apple")

'''
Typecasting:-

list,set, tuple
str->int
int->float

'''
# word = "python"
int1 = 10
res = str(int1)    # int -> str
print(type(res))

list1 = [1,2,3,4]
print(list1)
print(type(list1))

list1 = set(list1)
print(list1)
print(type(list1))

fruits = ("apple","mango","banana","cherry")
# fruits = ("apple","mango","banana","cherry","grapes")
# you have to add grapes at the end of the tuple 
# 
# fruits = ("apple","mango","banana","cherry")
# fruitlist=list(fruits)
# print(fruitlist.append("grapes"))
# print(tuple(fruitlist))
   
# packing unpacking

fruits = ("apple","mango","banana","cherry","grapes")  #packing
numbers = (1,2,3)
print(fruits+numbers)
# (one,*two,three) = fruits             #unpacking


# # asterix *  method
# print(one)
# print(two)
# print(three)


'''
set :- {}
mutable/
unorderd,unindexed,unchangeable (you can add or remove the values) 
duplications are not allowed in set

'''
set1 = {"apple","mango","banana","cherry"}
# set1.add("grapes")
set1.remove("grapes")
print(set1)
result = frozenset(set1)


'''
Dict :- {key:value}
dict are ordered  3.7 only
3.6  dict are unordered
Imp******
'''

num = {
    1:"one",
    2:"two",
    3:"three",
    4:[1,2,3,4,5,6,7,9],
    }

print((num[4]))

state = num.values()
print(state)
# print(state[2])

'''

Method	            Description
clear()	            Removes all the elements from the dictionary
copy()	            Returns a copy of the dictionary
fromkeys()          Returns a dictionary with the specified keys and value
get()	            Returns the value of the specified key
items()         	Returns a list containing a tuple for each key value pair
keys()	            Returns a list containing the dictionary's keys
pop()	            Removes the element with the specified key
popitem()           Removes the last inserted key-value pair
setdefault()        Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	        Updates the dictionary with the specified key-value pairs
values()	        Returns a list of all the values in the dictionary



'''