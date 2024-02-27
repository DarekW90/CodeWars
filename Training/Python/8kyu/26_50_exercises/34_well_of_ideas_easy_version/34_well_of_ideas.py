def well(x):
    idea = int()
    for i in x:
        if i == "good":
            idea += 1

    if idea == 0:
        idea = "Fail!"
    elif idea >= 3:
        idea = "I smell a series!"
    else:
        idea = "Publish!"

    return idea


test1 = well(['bad', 'bad', 'bad'])
test2 = well(['good', 'bad', 'bad', 'bad', 'bad'])
test3 = well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good'])


print(f"{test1} # 'Fail!'")
print(f"{test2} # 'Publish!'")
print(f"{test3} # 'I smell a series!'")