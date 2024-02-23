def cube_checker(volume, side):
    return 0 < volume == side**3


test1 = cube_checker(-12, 2)
test2 = cube_checker(8, 2)
test3 = cube_checker(0, 0)
test4 = cube_checker(-12, -1)
test5 = cube_checker(8, 3)

print(f"{test1} # False")
print(f"{test2} # True")
print(f"{test3} # False")
print(f"{test4} # False")
print(f"{test5} # False")
