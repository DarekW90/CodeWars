def repeat_str(repeat, string):
    return string*repeat




test1 = repeat_str(4, 'a')
test2 = repeat_str(3, 'hello ')
test3 = repeat_str(2, 'abc')


print(f"{test1} # aaaa")
print(f"{test2} # hello hello hello ")
print(f"{test3} # abcabc")