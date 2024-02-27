from functools import reduce
def grow1(arr):
    return reduce(lambda x, y: x * y, arr)


import math
def grow2(arr):
    return math.prod(arr)


test1 = grow1([1, 2, 3])
test2 = grow1([4, 1, 1, 1, 4])
test3 = grow1([2, 2, 2, 2, 2, 2])

test4 = grow2([1, 2, 3])
test5 = grow2([4, 1, 1, 1, 4])
test6 = grow2([2, 2, 2, 2, 2, 2])

print(f"{test1} # 6")
print(f"{test2} # 16")
print(f"{test3} # 64")

print(f"{test4} # 6")
print(f"{test5} # 16")
print(f"{test6} # 64")

