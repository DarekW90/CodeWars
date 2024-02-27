def divisible_by(numbers, divisor):
    nums = []
    for i in numbers:
        if i % divisor == 0:
            nums.append(i)
    return nums


test1 = divisible_by([1, 2, 3, 4, 5, 6], 2)
test2 = divisible_by([1, 2, 3, 4, 5, 6], 3)
test3 = divisible_by([0, 1, 2, 3, 4, 5, 6], 4)
test4 = divisible_by([0], 4)
test5 = divisible_by([1, 3, 5], 2)
test6 = divisible_by([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)



print(f"{test1} # [2, 4, 6]")
print(f"{test2} # [3, 6]")
print(f"{test3} # [0, 4]")
print(f"{test4} # [0]")
print(f"{test5} # []")
print(f"{test6} # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")