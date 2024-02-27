def flip(d,a):
    return sorted(a, reverse=d=='L')


test1 = flip('R', [3, 2, 1, 2])
test2 = flip('L', [1, 4, 5, 3, 5])


print(f"{test1} # [1, 2, 2, 3]")
print(f"{test2} # [5, 5, 4, 3, 1]")