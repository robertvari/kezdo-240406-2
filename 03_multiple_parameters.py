def say_hello(address, age, name):
    print(f"Hello {name}!")
    print(f"You live in {address}.")
    print(f"You are {age} years old.")


say_hello("Csaba", "Budapest", 32)

# keyword parameters
say_hello(age=32, name="Csaba", address="Budapest")