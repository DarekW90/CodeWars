def monkey_count(n):
    return list(range(1, n+1))


test1 = monkey_count(5)
test2 = monkey_count(3)
test3 = monkey_count(9)
test4 = monkey_count(10)
test5 = monkey_count(20)


print(f"{test1} # [1, 2, 3, 4, 5]")
print(f"{test2} # [1, 2, 3]")
print(f"{test3} # [1, 2, 3, 4, 5, 6, 7, 8, 9]")
print(f"{test4} # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
print(f"{test5} # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]")