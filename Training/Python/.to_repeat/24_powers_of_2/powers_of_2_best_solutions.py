def powers_of_two(n):
    return [2**x for x in range(n+1)]


test1 = powers_of_two(0)
test2 = powers_of_two(1)
test3 = powers_of_two(4)

print(f"{test1} # [1]")
print(f"{test2} # [1, 2]")
print(f"{test3} # [1, 2, 4, 8, 16]")
