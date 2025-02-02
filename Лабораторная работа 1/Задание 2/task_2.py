from task_1 import Tree, Book, Stack# TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
 # TODO: инстанцировать все описанные классы, создав три объекта.C()
    tree  = Tree(25, 7.5)
    book  = Book("I Robot", 304)
    stack = Stack()
    try:
     # TODO: вызвать метод с некорректными аргументами(b)
        tree.grow(-1)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
     # TODO: вызвать метод с некорректными аргументами(a)
        book.turn_page(500)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
     # TODO: вызвать метод с некорректными аргументами(a)
     stack.push("5")
    except TypeError:
        print('Ошибка: неправильные данные')

