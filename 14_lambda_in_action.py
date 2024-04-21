my_friends = ["Vári Róbert", "Kiss Balázs", "Kovács Elemér", "Tóth Krisztina", "Kiss Csaba Géza"]

def get_name_for_sorting(name):
    return name.split()[-1]

# function reference
# get_name_for_sorting

# function call
# get_name_for_sorting()

default_sorting = sorted(my_friends)
modified_sorting = sorted(my_friends, key=get_name_for_sorting)
modified_sorting_lambda = sorted(my_friends, key=lambda name : name.split()[-1])
print(default_sorting)
print(modified_sorting)
print(modified_sorting_lambda)