def get_average(marks):
    return sum(marks) // len(marks)


test1 = get_average([2, 2, 2, 2])
test2 = get_average([1, 5, 87, 45, 8, 8])
test3 = get_average([2,5,13,20,16,16,10])
test4 = get_average([1,2,15,15,17,11,12,17,17,14,13,15,6,11,8,7])

print(f"{test1} # 2")
print(f"{test2} # 25")
print(f"{test3} # 11")
print(f"{test4} # 11")
