def year_days(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return f'{year} has 366 days'
    return f'{year} has 365 days'


test1 = year_days(0)
test2 = year_days(-64)
test3 = year_days(2016)
test4 = year_days(1974)
test5 = year_days(-10)
test6 = year_days(666)
test7 = year_days(1857)
test8 = year_days(2000)
test9 = year_days(-300)
test10 = year_days(-1)



print(f"{test1} #\t '0 has 366 days'")
print(f"{test2} #\t '-64 has 366 days'")
print(f"{test3} #\t '2016 has 366 days'")
print(f"{test4} #\t '1974 has 365 days'")
print(f"{test5} #\t '-10 has 365 days'")
print(f"{test6} #\t '666 has 365 days'")
print(f"{test7} #\t '1857 has 365 days'")
print(f"{test8} #\t '2000 has 366 days'")
print(f"{test9} #\t '-300 has 365 days'")