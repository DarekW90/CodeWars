def multiply(n):
  return n*5**len(str(abs(n)))


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
