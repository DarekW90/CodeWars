def flick_switch(lst):
    result = []
    switch = True

    for item in lst:
        if item == 'flick':
            switch = not switch
        result.append(switch)

    return result




test1 = flick_switch(['codewars', 'flick', 'code', 'wars'])
test2 = flick_switch(['flick', 'chocolate', 'adventure', 'sunshine'])
test3 = flick_switch(['bicycle', 'jarmony', 'flick', 'sheep', 'flick'])
test4 = flick_switch(['bicycle'])
test5 = flick_switch(['john, smith, susan', 'flick'])
test6 = flick_switch(['flick', 'flick', 'flick', 'flick', 'flick'])
test7 = flick_switch([])

print(f"{test1} # [True, False, False, False]")
print(f"{test2} # [False, False, False, False]")
print(f"{test3} # [True, True, False, False, True]")
print(f"{test4} # [True]")
print(f"{test5} # [True, False]")
print(f"{test6} # [False, True, False, True, False]")
print(f"{test7} # []")