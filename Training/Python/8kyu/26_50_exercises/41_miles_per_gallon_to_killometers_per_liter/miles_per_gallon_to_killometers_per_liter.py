def converter(mpg):
    return round((mpg * 1.609344) / 4.54609188, 2)


test1 = converter(10)
test2 = converter(20)
test3 = converter(30)
test4 = converter(24)
test5 = converter(36)


print(f"{test1} # 3.54")
print(f"{test2} # 7.08")
print(f"{test3} # 10.62")
print(f"{test4} # 8.50")
print(f"{test5} # 12.74")