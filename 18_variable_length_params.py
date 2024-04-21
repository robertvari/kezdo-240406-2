def variable_lenght_params(*args, **kwargs):
    print(args)
    print(kwargs)

# variable_lenght_params("Robert", "Csaba", "Kriszta", 120, 2313213)
# variable_lenght_params(name="Robert", address="Budapest", phone="0620 123 4567")
variable_lenght_params("Robert", "Csaba", "Kriszta", 120, 2313213, name="Robert", address="Budapest", phone="0620 123 4567")