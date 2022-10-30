from functools import reduce

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(reduce(lambda a, b: a if a > b else b, lis))


# ---------------------------------------------------------
# 6