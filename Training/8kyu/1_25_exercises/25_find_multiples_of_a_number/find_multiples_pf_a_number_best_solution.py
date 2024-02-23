def find_multiples(integer, limit):
    return list(range(integer, limit+1, integer))


test1 = find_multiples(5, 25)
test2 = find_multiples(1, 2)

print(f"{test1} # [5, 10, 15, 20, 25]")
print(f"{test2} # [1, 2]")