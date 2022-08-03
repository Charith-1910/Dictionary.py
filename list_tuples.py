# list = ['abcd' , 896 , 3.53 , 'charith' , 80.9 ]
# tinylist = [321 , 'john']
# print(list)            #prints complete list
# print(list[0])         #prints first element of the list
# print(list[1:3])       #prints elements starting from 2nd till 3rd
# print(list[2:])        #print elements starting from 3rd
# print(tinylist * 2)    #prints list 2 times
# print(list + tinylist) #prints both the lists
#
#
# list1 = [10, 20, 23, 32, 45, 90]
# #print the largest number in list
# print("largest element is:", max(list1))
# print(max(list1))
#
#
# tuple = ['abcd' , 896 , 3.53 , 'charith' , 80.9 ]
# tinytuple = [321 , 'john']
# print(tuple)            #prints complete tuple
# print(tuple[0])         #prints first element of the tuple
# print(tuple[1:3])       #prints elements starting from 2nd till 3rd
# print(tuple[2:])        #print elements starting from 3rd
# print(tinytuple * 2)    #prints tuple 2 times
# print(tuple + tinytuple) #prints both the tuple
#
#
# dict = {}
# dict['one'] = "this is one"
# dict[2]     = "this is two"
# tinydict = {'name':'john' , 'code':6734 , 'dept':'sales'}
# print(dist['one'])     #prints value for 'one' key
# print(dict[2])         #prints value for 2 key
# print(tinydict)        #prints complete dictionary
# print(tinydict.keys()) #prints all the keys
#
#
# str = "pfsd"
# print(len(str)) #prints the length of the string
#
# s = 'PFSD CSEH Students'
# #print the string after split method
# print(s.split(" "))
# #print the string after join method
# print("-".join(s.split()))
#
#
# list1 = [1, 2, 3, 4, 5]
# #using sum() function
# total = sum(list1)
# #printing total vlaue
# print("sum of all elements in given list: ", total)
#

# class Person :
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#   def printname(self):
#     print(self.firstname, self.lastname)
#
# x = Person("Cse", "pfsd")
# x.printname()

# class Parent:
#     def __init__(self,txt):
#         self.message = txt
#     def printmessage(self):
#         print(self.message)
#
# class Child(Parent):
#     def __int__(self,txt):
#         super().__init__(txt)
# x = Child("hello, and welcome!")
# x.printmessage()

# # Random Functions
# import random
# n=random.randbytes(3)
# print(n)
# print(random.randrange(1,8))
# print(random.randint(100,211))
# mylist = ["Jadeja", "Aswin","Rahene", "Shami","Dhoni", "Virat"]
# mylist1 =["Jadeja", "Aswin","Rahene", "Shami","Dhoni", "Virat"]
# print(random.choice(mylist))
# #print(random.choice(mylist1))
# random.shuffle(mylist)

# # MATCHING EXPRESSIONS
# import re
# txt = "Use of python in Machine Learning"
# x = re.search("^Use.*Learning", txt)
# if(x) :
#     print("YES! We have a match")
# else:
#     print("No match")

# # MATCHING EXPRESSIONS
# import re
# txt = "Use of python in Machine Learning"
# x = re.findall("in",txt)
# print(x)

# MATCHING EXPRESSIONS
import re
txt = "Python is one of the most popular languages"
searchobj  = re.search("\s",txt)
print("The frist white-space character is located")

