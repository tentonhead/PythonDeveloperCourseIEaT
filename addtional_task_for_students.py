# TODO Написать свою реализацию функции для подсчёта числа вхождение элементов в список
def my_count(l: list, item):
    count = 0
    for i in l:
        if i == item:
            count += 1
    return count

"""
items = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 10]
print(my_count(items, 1))
print(my_count(items, 8))

items = ["d", "s", "B", "g", "g"]
print(my_count(items, "b"))
print(my_count(items, "g"))
"""
