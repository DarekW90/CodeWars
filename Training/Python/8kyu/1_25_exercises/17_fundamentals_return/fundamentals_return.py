def add(a, b):
    return a+b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def mod(a, b):
    return a%b

def exponent(a, b):
    return a**b

def subt(a, b):
    return a-b


test1 = add(1, 2)
test2 = multiply(1, 2)
test3 = divide(2, 1)
test4 = mod(1, 2)
test5 = exponent(1, 2)
test6 = subt(1, 2)

print(f"{test1} # 3")
print(f"{test2} # 2")
print(f"{test3} # 2")
print(f"{test4} # 1")
print(f"{test5} # 1")
print(f"{test6} # -1")