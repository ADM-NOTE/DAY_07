def describe_person(*args, **kwargs):
    print("Позиционные аргументы:")
    for i in args:
        print(i)
    print("Именованные аргументы: ")
    for key, value in kwargs.items():
        print(key, ":", value)


describe_person(1, 2, 3, 4, name = "AKRAM")    