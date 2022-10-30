def is_greater_than_4(num):
    # return true if num>4 else return false
    return num > 4


listt = [1, 2, 3, 4, 5, 6, 7, 8, 9]
greaterThan4 = list(filter(is_greater_than_4, listt))
print(greaterThan4)


# -----------------------------------------------------
# [5, 6, 7, 8, 9]
