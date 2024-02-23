def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)


test1 = array_plus_array([1, 2, 3], [4, 5, 6])
test2 = array_plus_array([-1, -2, -3], [-4, -5, -6])
test3 = array_plus_array([0, 0, 0], [4, 5, 6])
test4 = array_plus_array([100, 200, 300], [400, 500, 600])

print(f"{test1} # 21")
print(f"{test2} # -21")
print(f"{test3} # 15")
print(f"{test4} # 2100")
