def count_positives_sum_negatives(arr):
    count_positives = 0
    sum_negatives = 0

    if not arr:
        return []

    for i in arr:
        if i > 0 and i != 0:
            count_positives += 1
        else:
            sum_negatives += i

    return [count_positives, sum_negatives]


test1 = count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
test2 = count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14])
test3 = count_positives_sum_negatives([1])
test4 = count_positives_sum_negatives([-1])
test5 = count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0])
test6 = count_positives_sum_negatives([])


print(f"{test1} # [10, -65]")
print(f"{test2} # [8, -50]")
print(f"{test3} # [1, 0]")
print(f"{test4} # [0, -1]")
print(f"{test5} # [0, 0]")
print(f"{test6} # []")
