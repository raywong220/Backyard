# # students = [[input(), float(input())] for i in range(int(input()))]
# students = [["r", 13.0], ["a", 17.0], ["y", 89.0], ["m", 55.0], ["o", 22]]
# students.insert(2, ["n", 22])
# # try:
# #     students.remove(["r", 13.0])
# # except:
# #     print("Not found")
#############################################
# # Find specific item in list and count the number of appearance
# def countlist(ls, wordtofind):
#     return sum(wordtofind in i for i in ls)

#############################################
# lowest_mark = float("inf")
# seclow_mark = float("inf")
# lowest_name = []
# seclow_name = []

# for i in range(int(input("Number of entry:"))):
#     name = input("Name:")
#     marks = int(input("Marks:"))

#     if marks < lowest_mark:
#         seclow_mark = lowest_mark
#         lowest_mark = marks
#         seclow_name = lowest_name
#         lowest_name.append(name)
#     elif marks == lowest_mark:
#         lowest_name.append(name)
#     elif marks < seclow_mark:
#         seclow_mark = marks
#         seclow_name = name
#     elif marks == seclow_name:
#         seclow_name.append(name)

# print(sorted([name for name in seclow_name]))
###################################################

# marksheet = []
# for _ in range(int(input())):
#     marksheet.append([input(), float(input())])

# # Equal to # #

# marksheet = [
#     [input("Name:"), float(input("Marks:"))] for _ in range(int(input("# Entries: ")))
# ]
# second_lowest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print("\n".join([name for name, marks in sorted(marksheet) if marks == second_lowest]))

####################################################


# a = {"one": 1, "two": "to", "three": 3.0, "four": [4, 4.0]}
# print(a)
# a["one"] = 2
# print(a)
# del a["one"]
# print(a)
# a.clear()  # remove the content
# print(a)
# del a  # remove the entire dict

# b = [1, 2, 3]
# b[0] = 2
# print(b)
# del b[0]
# print(b)
# # del b  - remove the list entirely

# sweet_dict = {"a1": "cake", "a2": "cookie", "a1": "icecream"}
# print(sweet_dict)  # ignore the first duplicated key a1

##################################################
# dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
# print(dict1.items())
# print(dict1.keys())
# print(dict1.values())
## dicionary comprehensions

## create new dict from old dict
## dict2 = {key:value for (key,v) in dict1.items()}

## create a new dict where value is the square of the key
## dict1 = {k: k**2 for k in range(10) if k % 2 ==0}

##############################################
## Using Lambda to convert F to C and make a dict
# fahrenheit = {"t1": -30, "t2": -20, "t3": -10, "t4": 0}
# celsius = list(map(lambda x: 5 / 9 * (x - 32), fahrenheit.values()))
# celsius_dict = dict(zip(fahrenheit.keys(), celsius))
# print(celsius_dict)

## Alternate to the above Lambda function
# fahrenheit = {"t1": -30, "t2": -20, "t3": -10, "t4": 0}
# celsius_dict = {k: (5 / 9 * (v - 32)) for (k, v) in fahrenheit.items()}
# print(celsius_dict)

############################################
## Dict comprehension with multiple if statement
# dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
# dict2 = {k: v for (k, v) in dict1.items() if v >= 2 if v % 2 == 0}
# print(dict2)

## If-else
# dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
# dict2 = {k: ("even" if v % 2 == 0 else "odd") for (k, v) in dict1.items()}
# print(dict1)
# print(dict2)

###########################################
# num1 = {k: k ** 3 for k in range(16) if k % 2 == 0}
# num2 = {k: k ** 2 for k in range(16) if k % 2 == 1}
# num3 = {**num1, **num2}
# print("num1:", num1)
# print("num2:", num2)

###
## Sort by key
# num3 = {k: num3[k] for k in sorted(num3)}
# num3 = {k: v for k, v in sorted(num3.items())}

## Sort by value
# num3 = {k: v for k, v in sorted(num3.items(), key=lambda item: item[1])}
# num3 = {k: num3[k] for k in sorted(num3, key=num3.get)}
# print(num3)
############################################
# num1 = {k: k ** 3 for k in range(16) if k % 2 == 0}
# print(num1)
# key_sum = sum(num1.keys())
# value_sum = sum(num1.values())
# print(key_sum, value_sum)

# from functools import reduce

# my_dict = {"data1": 100, "data2": -54, "data3": 247}
# print(reduce(lambda x, y: x * y, my_dict.values()))
############################################

# d = {1}
# print("empty" if not bool(d) else "full")

#############################################
# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {"a": 300, "b": 200, "d": 400}
# d3 = {"b": 300, "c": 200, "d": 400}


# def addDict(d1: dict, d2: dict) -> dict:
#     d = d1.copy()
#     for k, v in d2.items():
#         if not k in d1:
#             d[k] = v
#         else:
#             d[k] += v
#     d = {k: d[k] for k in sorted(d)}
#     return d


## Same as
# def addDict(d1: dict, d2: dict) -> dict:
#     d = d1.copy()
#     d.update({k: (d1[k] + v if k in d1 else v) for k, v in d2.items()})
#     d = {k: d[k] for k in sorted(d)}
#     return d


# d = addDict(d1, d2)
# print(d)


#### IMPORTANT ####
## Add the value if the key appears in both dict otherwise insert into the first dict
# d1.update({k: (d1[k] + v if k in d1 else v) for k, v in d2.items()})

# # Same but in this case the original two dicts not affected
# d3 = d1.copy()  # <---- use copy method to avoid passing by reference in Python
# d3.update({k: (d1[k] + v if k in d1 else v) for k, v in d2.items()})
# print(d1, d2, d3)

### Using module to do the same operation
# from collections import Counter

# d3 = dict(Counter(d1) + Counter(d2))
# print(type(d3))
# print(d3)

### Sorting both keys and values
# num = {"n2": [5, 1, 2], "n1": [2, 3, 1], "n3": [3, 2, 4]}
# num = {k: sorted(num[k]) for k in sorted(num)}
# print(num)

### Sort by value and print three highest value
# data = {"item1": 45.50, "item2": 35, "item3": 41.30, "item4": 55, "item5": 24}
# high = sorted(data, key=data.get, reverse=True)[:3]
# for k in high:
#     print(k, data[k])

### Count the total number of items in all values
# dict = {"Alex": ["subj1", "subj2", "subj3"], "David": ["subj1", "subj2"]}
# print(sum(map(len, dict.values())))

student_details = [
    {"id": 1, "subject": "math", "V": 70, "VI": 82},
    {"id": 2, "subject": "math", "V": 73, "VI": 74},
    {"id": 3, "subject": "math", "V": 75, "VI": 86},
]


def aver(list):
    for dict in list:
        v = dict.pop("V")
        vi = dict.pop("VI")
        dict["V+VI"] = (v + vi) / 2
    return list


print(aver(student_details))