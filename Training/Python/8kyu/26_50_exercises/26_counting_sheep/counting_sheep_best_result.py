def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)


array1 = [True,  True,  True,  False,
          True,  True,  True,  True,
          True,  False, True,  False,
          True,  False, False, True,
          True,  True,  True,  True,
          False, False, True,  True]

test1 = count_sheeps(array1)

print(f"There are {test1} - 17 sheeps in total")