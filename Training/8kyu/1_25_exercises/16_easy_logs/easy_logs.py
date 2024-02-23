import math


def logs(x, a, b):
    sum_log = math.log(a, x) + math.log(b, x)
    return sum_log


test1 = logs(10, 2, 3)
test2 = logs(5, 2, 3)
test3 = logs(1000, 2, 3)
test4 = logs(2, 1, 2)
test5 = logs(0.00001, 0.002, 0.01)
test6 = logs(0.1, 0.002, 0.01)


print(f"{test1} # 0.7781512503836435")
print(f"{test2} # 1.1132827525593785")
print(f"{test3} # 0.25938375012788123")
print(f"{test4} # 1")
print(f"{test5} # 0.9397940008672038")
print(f"{test6} # 4.69897000433602")
