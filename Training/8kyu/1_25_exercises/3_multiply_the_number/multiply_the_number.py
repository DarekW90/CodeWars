def multiply(n):
    # Convert numbers to absolute value to remove the minus sign
    n_abs = abs(n)

    # Change number to string and count number of characters
    x = len(str(n_abs))

    # Bring results ((number*5)**length of string)
    result = n * 5 ** x

    return result


check1 = multiply(10)
check2 = multiply(5)
check3 = multiply(200)
check4 = multiply(0)
check5 = multiply(-2)

print(f"{check1} # 250")
print(f"{check2} # 25")
print(f"{check3} # 25000")
print(f"{check4} # 0")
print(f"{check5} # -10")
