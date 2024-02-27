def count_squares(x):
    return  (x + 1) ** 3 - (x - 1) ** 3


test000 = count_squares(0)
test00 = count_squares(1)
test0a = count_squares(2)
test0b = count_squares(4)
test1 = count_squares(5)
test2 = count_squares(16)
test3 = count_squares(23)


print(f"{test000} # 1")
print(f"{test00} # 8")
print(f"{test0a} # 26")
print(f"{test0b} # 98")
print(f"{test1} # 152")
print(f"{test2} # 1538")
print(f"{test3} # 3176")
