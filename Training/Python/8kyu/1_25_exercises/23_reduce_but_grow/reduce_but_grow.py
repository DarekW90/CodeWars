def grow(arr):
    result = 1
    for x in arr:
        result = result * x
    return result


test1 = grow([1, 2, 3])
test2 = grow([4, 1, 1, 1, 4])
test3 = grow([2, 2, 2, 2, 2, 2])

print(f"{test1} # 6")
print(f"{test2} # 16")
print(f"{test3} # 64")

