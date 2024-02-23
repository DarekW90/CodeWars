def collinearity(x1, y1, x2, y2):
    return x1 * y2 == x2 * y1


test1 = collinearity(1, 1, 1, 1)
test2 = collinearity(1, 2, 2, 4)
test3 = collinearity(1, 1, 6, 1)
test4 = collinearity(1, 2, -1, -2)
test5 = collinearity(1, 2, 1, -2)
test6 = collinearity(4, 0, 11, 0)
test7 = collinearity(0, 1, 6, 0)
test8 = collinearity(4, 4, 0, 4)
test9 = collinearity(0, 0, 0, 0)
test10 = collinearity(0, 0, 1, 0)
test11 = collinearity(5, 7, 0, 0)

print(f"Test 1\t{test1} # True")
print(f"Test 2\t{test2} # True")

print(f"Test 3\t{test3} # False")
print(f"Test 4\t{test4} # True")
print(f"Test 5\t{test5} # False")

print(f"Test 6\t{test6} # True")
print(f"Test 7\t{test7} # False")
print(f"Test 8\t{test8} # False")

print(f"Test 9\t{test9} # True")
print(f"Test 10\t{test10} # True")
print(f"Test 11\t{test11} # True")
