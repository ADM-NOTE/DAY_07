def sort_by_age(people):
    return sorted(people, key = lambda x: x[1])

people = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]

sort = sort_by_age(people)

print(sort)
