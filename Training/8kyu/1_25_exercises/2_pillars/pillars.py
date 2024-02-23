def pillars(num_pill, dist, width):

    # Change distance input to centimeters
    dist_meters = dist * 100

    # Calculate the total distance between pillars
    total_dist = (num_pill - 1) * dist_meters

    # Subtract width of first and last pillar
    if num_pill >= 3:
        total_dist += (num_pill * width) - (2*width)

    return total_dist


check1 = pillars(1, 10, 10)
print(f"{check1} # 0")

check2 = pillars(2, 20, 25)
print(f"{check2} # 2000")

check3 = pillars(11, 15, 30)
print(f"{check3} # 15270")
