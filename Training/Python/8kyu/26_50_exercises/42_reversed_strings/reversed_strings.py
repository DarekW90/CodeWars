def solution(string):
    return string[::-1]


test1 = solution('world')
test2 = solution('hello')
test3 = solution('')
test4 = solution('h')

print(f"{test1} # 'dlrow'")
print(f"{test2} # 'olleh'")
print(f"{test3} # ''")
print(f"{test4} # 'h'")