def cannons_ready(gunners):
    value_count = []
    for _, value in gunners.items():
        if value == 'aye':
            value_count.append(value)

    if len(value_count) == len(gunners):
        return "Fire!"
    else:
        return "Shiver me timbers!"


a = {'Mike': 'aye', 'Joe': 'aye', 'Johnson': 'aye', 'Peter': 'aye'}
b = {'Mike': 'aye', 'Joe': 'nay', 'Johnson': 'aye', 'Peter': 'aye'}
c = {'Joe': 'nay', 'Johnson': 'nay', 'Peter': 'aye'}
d = {'Mike': 'nay', 'Joe': 'nay', 'Johnson': 'nay', 'Peter': 'nay'}

test1 = cannons_ready(a)
test2 = cannons_ready(b)
test3 = cannons_ready(c)
test4 = cannons_ready(d)

print(f"{test1} # 'Fire!'")
print(f"{test2} # 'Shiver me timbers!")
print(f"{test3} # 'Shiver me timbers!")
print(f"{test4} # 'Shiver me timbers!")
