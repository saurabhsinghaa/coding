from functools import reduce
listt = [1, 2, 3, 4]  # sum is 10
list_sum = reduce(lambda x, y: x+y, listt)
print(list_sum)

# -------------------------------------------
# 10