# List MUTATION
L = [1, 2] + [3, 4]  # concatenate 2 lists
print(L)
# add elements to the end (a sublist in this case)
L.append([5, 6])  # MUTATES
print(L)
# Extend! Split string into char and add at the end of list
L.extend("red")  # MUTATES
print(L)
# remove the first appearance of the argument, give error if not on list
L.remove("r")  # MUTATES
print(L)
f = L.pop()  # remove and return the last element
print(L)
print(f)
del L[4]  # delete the element at the specific index
print(L)

print("-----------------")
# String <--> List Conversion
n = "ab c"
print(n)
# convert STRING to list, RETURN a LIST with every element
print(list(n))
# split a STRING, RETURN a LIST on spaces, on character when with parameter
n = n.split()
print(n)

L = ["a", "b", "c"]
# turn a LIST of char into a STRING, insert char in quote in every element
a = "".join(L)
print(a)
a = "_".join(L)
print(a)
print("-----------------")

# Sort() and Sorted()
N = [9, 6, 0, 3]
N2 = sorted(N)  # RETURN sorted list, does NOT MUTATE original list
print(N2)
N.sort()  # MUTATES the list
print(N)
N.reverse()  # MUTATES the list
print(N)


# Integer is a NON mutable object, variable a is not affected by the change of b
a = 1
b = a
b = 3
print(a)
# Also Tuple
a = (1, 2, 3)
b = a
b = (2, 3, 4)
print(a)
# Also String
a = "2"
b = a
b += "3"
print(a)
print("---------------")
# However, LIST is MUTABLE : Append will mutate the list
print("In List case, it is mutable")
a = [2, 3]
b = a  # b is the alias of a
b.append(4)
print("b", b)
print("a", a)

print("If we want a new copy of the list, we can CLONE it")
a = [2, 3]
b = a[:]  # through [:] notation specify coloing
b.append(4)
print("b", b)
print("a", a)

print("---------------")
print("EXTREMELY IMPORTANT")
print("How the following 2 function mutate L1 content?")


def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)


def remove_dups2(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)


L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2)
print("Version 1:", "L1", L1, "L2", L2)
L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups2(L1, L2)
print("Version 2:", "L1", L1, "L2", L2)
"""
The first one doesnt remove 2 because the for loop counter 
didnt update the index X(L1[0] -> L1[0]) in the second iteration.
As 2 become the new L1[0] after the first removal (1),
the next iteration begins on L1[1] (3)

While the second version of the function is different,
it begins with making a copy of L1 (L1_copy).
Therefore while looping over L1_copy, removal of 1 of L1
will not affect L1_copy, thus the internal index counter
"""
