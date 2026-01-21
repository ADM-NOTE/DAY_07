def sum_all(*args):
    a = 0
    for i in args:
        a += i
    return a

print(sum_all(1, 2, 3, 4))