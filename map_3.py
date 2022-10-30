def iterate(a):
    return a


def cube(a):
    return a*a*a


func = [iterate, cube]
for i in range(1, 6):
    val = list(map(lambda x: x(i), func))
    print(val)

# ------------------------------------------
# [1, 1]
# [2, 8]
# [3, 27]
# [4, 64]
# [5, 125]