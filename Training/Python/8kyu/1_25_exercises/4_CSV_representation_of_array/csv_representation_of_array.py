def to_csv_text(array):
    csv_str = ""
    for row in array:
        csv_str += ",".join(map(str,row)) + "\n"

    return csv_str.rstrip("\n")


check1 = to_csv_text([
    [0, 1, 2, 3, 45],
    [10, 11, 12, 13, 14],
    [20, 21, 22, 23, 24],
    [30, 31, 32, 33, 34]
    ])

# "0,1,2,3,45\n10,11,12,13,14\n20,21,22,23,24\n30,31,32,33,34",

print(check1)
