def is_uppercase(inp):
    for i in inp:
        if i.islower():
            return False
    return True


test1 = is_uppercase("c")
test2 = is_uppercase("C")
test3 = is_uppercase("hello I AM DONALD")
test4 = is_uppercase("HELLO I AM DONALD")
test5 = is_uppercase("$%&")

print(f"{test1} # False")
print(f"{test2} # True")
print(f"{test3} # False")
print(f"{test4} # True")
print(f"{test5} # True")
