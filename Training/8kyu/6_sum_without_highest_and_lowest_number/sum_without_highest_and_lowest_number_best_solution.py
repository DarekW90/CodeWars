def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)


check1 = sum_array([6, 2, 1, 8, 10])
check2 = sum_array([6, 0, 1, 10, 10])
check3 = sum_array([-6, -20, -1, -10, -12])
check4 = sum_array([-6, 20, -1, 10, -12])
check5 = sum_array([3])
check6 = sum_array([-3])
check7 = sum_array([])


print(f"Check1: {check1} # 16")
print(f"Check2: {check2} # 17")
print(f"Check3: {check3} # -28")
print(f"Check4: {check4} # 3")
print(f"Check5: {check5} # 0")
print(f"Check6: {check6} # 0")
print(f"Check7: {check7} # 0")
