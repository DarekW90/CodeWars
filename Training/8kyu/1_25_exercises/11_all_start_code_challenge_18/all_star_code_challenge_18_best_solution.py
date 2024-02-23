def str_count(string, letter):
    return string.count(letter)


test1 = str_count('hello', 'l')
test2 = str_count('hello', 'e')
test3 = str_count('codewars', 'c')
test4 = str_count('ggggg', 'g')
test5 = str_count('hello world', 'o')
test6 = str_count('', 'z')


print(f"{test1} # 2")
print(f"{test2} # 1")
print(f"{test3} # 1")
print(f"{test4} # 5")
print(f"{test5} # 2")
print(f"{test6} # 0")
