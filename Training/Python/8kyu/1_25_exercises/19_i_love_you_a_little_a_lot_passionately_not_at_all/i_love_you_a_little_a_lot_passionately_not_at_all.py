def how_much_i_love_you(nb_petals):
    arr = [("I love you"),
           ("a little"),
           ("a lot"),
           ("passionately"),
           ("madly"),
           ("not at all")]

    search_for_index = nb_petals % len(arr)

    return arr[search_for_index-1]


test1 = how_much_i_love_you(7)
test2 = how_much_i_love_you(3)
test3 = how_much_i_love_you(6)

print(f"{test1} # I love you")
print(f"{test2} # a lot")
print(f"{test3} # not at all")
