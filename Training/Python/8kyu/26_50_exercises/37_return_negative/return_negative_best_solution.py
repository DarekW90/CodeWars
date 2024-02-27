def make_negative( number ):
    return -abs(number)


test1 = make_negative(42)
test2 = make_negative(-9)
test3 = make_negative(0)

print(f"{test1} # -42")
print(f"{test2} # -9")
print(f"{test3} # 0")