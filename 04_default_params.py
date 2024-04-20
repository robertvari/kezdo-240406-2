def say_hello(name, address=None, age=None):
    print(f"Hello {name}!")

    if address:
        print(f"You live in {address}.")
    
    if age:
        print(f"You are {age} years old.")


say_hello(name="Csaba", address="Budapest", age=32)