def say_hello(name: str, address: str, age: int):
    """
    This function prints out user data.

    Parameters:
        name (str): User name.
        address (str): User address.
        age (int): User age.
    """

    print(f"Hello {name}!")
    print(f"You live in {address}.")
    print(f"You are {age} years old.")


say_hello("Robert", "Budapest", 32)