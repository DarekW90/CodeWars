def well(x):
    c = x.count('good')
    return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'


test1 = well(['bad', 'bad', 'bad'])
test2 = well(['good', 'bad', 'bad', 'bad', 'bad'])
test3 = well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good'])


print(f"{test1} # 'Fail!'")
print(f"{test2} # 'Publish!'")
print(f"{test3} # 'I smell a series!'")