# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

n_set = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ans = set()
times = 2000
print("started")
for i in range(times):
    for j in range(times - i):
        a_set = []
        k = i * j
        for m in str(i), str(j), str(k):
            m = [int(d) for d in m]
            a_set.extend(m)
        a_set = sorted(a_set)
        if n_set == a_set:
            ans.add(k)
            print(f"{k} = {i} * {j}")
print(ans)
print(sum(ans))