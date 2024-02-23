def sum_array(a):
    return sum(a)


test1 = sum_array([])
test2 = sum_array([1, 2, 3])
test3 = sum_array([1.1, 2.2, 3.3])
test4 = sum_array([4, 5, 6])
test5 = sum_array(range(101))


print(f"{test1} # 0")
print(f"{test2} # 6")
print(f"{test3} # 6.6")
print(f"{test4} # 15")
print(f"{test5} # 5050")