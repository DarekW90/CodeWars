def make_negative( number ):
    return number if number <= 0 else number*-1


test1 = make_negative(42)
test2 = make_negative(-9)
test3 = make_negative(0)

print(f"{test1} # -42")
print(f"{test2} # -9")
print(f"{test3} # 0")