def print_user(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


print_user(name = "AKRAM", age = 18)