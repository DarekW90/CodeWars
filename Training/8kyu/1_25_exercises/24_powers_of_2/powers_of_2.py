def powers_of_two(n):
    empty_list = []
    for i in range (n+1):
        pow_of_2 = 2 ** i
        empty_list.append(pow_of_2)
    return empty_list


test1 = powers_of_two(0)
test2 = powers_of_two(1)
test3 = powers_of_two(4)

print(f"{test1} # [1]")
print(f"{test2} # [1, 2]")
print(f"{test3} # [1, 2, 4, 8, 16]")
