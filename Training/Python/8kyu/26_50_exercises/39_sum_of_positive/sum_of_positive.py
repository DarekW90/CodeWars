def positive_sum(arr):
    sum = 0
    for i in arr:
        if i >= 0:
            sum += i
    return sum


test1 = positive_sum([1, 2, 3, 4, 5])
test2 = positive_sum([1, -2, 3, 4, 5])
test3 = positive_sum([-1, 2, 3, 4, -5])
test4 = positive_sum([])
test5 = positive_sum([-1, -2, -3, -4, -5])


print(f"{test1} # 15")
print(f"{test2} # 13")
print(f"{test3} # 9")
print(f"{test4} # 0")
print(f"{test5} # 0")