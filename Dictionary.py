# Dictionary is nothing but key value pairs
d1 = {}
print(type(d1))
d2 = {"Name":"charith",
      "Department":"CSE",
      "ID":"30542",
      "Food":{"B":"SeaFood", "L":"Drinks", "D":"JunkFood"}}
d2["Saiteja"] = "Junk Food"
d2[420] = "Kebabs"
d4 = {}
print(type(d4))
print(d2)
del d2[420]
print(d2["Mohan"])
d3 = d2.copy()
d2.update({"ID":255})
print(d2.keys())
print(d2.values())
print(d2.items())






# Convertions:-

# # list to dictionary
# l1=[1,2,3,4,5]
# l2=['a','b','c','d','e']
# d=dict(zip(l1,l2))
# print(d)


# # # dictionary to list
# d = {"name":"python", "version":3.9}
# new_list = list(d.items())
# print(new_list)


# # list to tuple
# data = ["KLSamyak", "Surabhi", "Include", "NationalGames", "EthnicDay"]
# print(data)

# data_tuple = tuple(data)
# print(data_tuple)


#
# # # tuple to list
# data = [1, 2, 3, "cat"]
# # # create list from tuple
# # ls = tuple(data)
# # print(ls)


# # List for keys and values in loop using dictionary
# dicts = {}
#
# keys = [10, 12, 14, 16]
# values = ["A", "B", "C", "D"]
#
# for i in range(len(keys)):
#     dicts[keys[i]] = values[i]
# print(dicts)


# Auto assign using key range
# dicts = {}
# keys = range(4)
# values = ["A", "B", "C", "D"]
# for i in keys:
#     dicts[i] = values[i]
# print(dicts)