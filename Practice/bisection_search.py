# reference: mit 6.0001
# # First implementation
# # O(log n) * O(n) => O(n log n)

# def bisect_search(L, e):
#     # constant O(1)
#     if L == []:
#         return False
#     # constant O(1)
#     elif len(L) == 1:
#         return L[0] == e
#     else:
#         # constant O(1)
#         half = len(L) // 2
#         if L[half] > e:
#             # not constant: copies list => O(n)
#             return bisect_search(L[:half], e)
#         else:
#             return bisect_search(L[half:], e)

# ==============================
# # Second implementation
# instead of copying the list in every call of recursion
# we keep track the low and high pointer of the list
# # O(log n)
def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)  # constant
        else:
            return bisect_search_helper(L, e, mid + 1, high)  # constant

    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)


# ====================================
# # Power Set
# Given a set of integers (with no repeats),  generate the
# collection of all possible subsets
# {1,2,3} -> {},{1},{2},{1,2},{3},{1,3},{2,3},{1,2,3}


def genSubset(L):
    if len(L) == 0:
        return [[]]
    # O(n): n -> n-1 -> n-2...
    smaller = genSubset(L[:-1])  # all subsets w/o last element
    extra = L[-1:]  # just last element
    new = []
    # a set of size k -> 2^k cases
    for small in smaller:
        new.append(small + extra)  # for all smaller solu, add each with last

    return smaller + new


print(genSubset([1, 2, 3, 4]))
