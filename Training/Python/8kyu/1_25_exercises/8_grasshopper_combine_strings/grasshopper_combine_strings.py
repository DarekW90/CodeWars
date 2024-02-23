def combine_names(name, surname):
    return f'{name} {surname}'


test1 = combine_names("James", "Stevens")
test2 = combine_names("Davy", "Back")
test3 = combine_names("Arthur", "Dent")


print(f'{test1} # "James Stevens"')
print(f'{test2} # "Davy Back"')
print(f'{test3} # "Arthur Dent"')
