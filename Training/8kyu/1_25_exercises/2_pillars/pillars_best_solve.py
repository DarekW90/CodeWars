def pillars(num_pill, dist, width):
    return dist * 100 * (num_pill - 1) + width * (num_pill - 2) * (num_pill > 1)


check1 = pillars(1, 10, 10)
print(f"{check1} # 0")

check2 = pillars(2, 20, 25)
print(f"{check2} # 2000")

check3 = pillars(11, 15, 30)
print(f"{check3} # 15270")
