def find_multiples(integer, limit):
    x = []

    for i in range(limit+1):
        if i % integer+1 == 1 and i != 0:
            x.append(i)

    return x


test1 = find_multiples(5, 25)
test2 = find_multiples(1, 2)

print(f"{test1} # [5, 10, 15, 20, 25]")
print(f"{test2} # [1, 2]")