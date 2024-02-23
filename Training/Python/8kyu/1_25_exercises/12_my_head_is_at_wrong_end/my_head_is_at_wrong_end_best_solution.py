def fix_the_meerkat(arr):
    return arr[::-1]


test1 = fix_the_meerkat(["tail", "body", "head"])
test2 = fix_the_meerkat(["tails", "body", "heads"])
test3 = fix_the_meerkat(["bottom", "middle", "top"])
test4 = fix_the_meerkat(["lower legs", "torso", "upper legs"])
test5 = fix_the_meerkat(["ground", "rainbow", "sky"])


print(f'{test1} # ["head", "body", "tail"]')
print(f'{test2} # ["heads", "body", "tails"]')
print(f'{test3} # ["top", "middle", "bottom"]')
print(f'{test4} # ["upper legs", "torso", "lower legs"]')
print(f'{test5} # ["sky", "rainbow", "ground"]')