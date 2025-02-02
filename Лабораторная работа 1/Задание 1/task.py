# TODO: Подробно описать три произвольных класса

class Glass:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Стакан"

        :param capacity_volume: Объем стакана
        :param occupied_volume: Объем занимаемой жидкости

        Примеры:
        >>> glass = Glass(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем стакана должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем стакана должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_glass(self) -> bool:
        """
        Функция которая проверяет является ли стакан пустым

        :return: Является ли стакан пустым

        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.is_empty_glass()
        """
        ...

    def add_water_to_glass(self, water: float) -> None:
        """
        Добавление воды в стакан.
        :param water: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в стакане, то вызываем ошибку

        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.add_water_to_glass(200)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна положительным числом")
        ...

    def remove_water_from_glass(self, estimate_water: float) -> None:
        """
        Извлечение воды из стакана.

        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в стакане,
        то возвращается ошибка.

        :return: Объем реально извлеченной жидкости

        Примеры:
        >>> glass = Glass(500, 500)
        >>> glass.remove_water_from_glass(200)
        """
        ...


# TODO: описать класс
class Tree:
    """Класс, описывающий дерево."""
    
    def __init__(self, age: int, height: float) -> None:
        """
        Инициализирует объект дерева.

        :param age: Возраст дерева в годах (должен быть неотрицательным).
        :param height: Высота дерева в метрах (должна быть положительной).
        :raises ValueError: Если возраст отрицательный или высота неположительная.
        """
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительной.")
        
        self.age = age
        self.height = height

    def grow(self, years: int) -> None:
        """
        Увеличивает возраст дерева и его высоту.

        :param years: Количество лет (должно быть положительным).
        :raises ValueError: Если передано неположительное количество лет.
        
        >>> tree = Tree(5, 2.0)
        >>> tree.grow(3)
        >>> tree.age
        8
        >>> tree.height
        2.9
        """
        if years <= 0:
            raise ValueError("Количество лет должно быть положительным.")
        
        self.age += years
        self.height += years * 0.3  # Примерный рост 30 см в год

    def is_old(self) -> bool:
        """
        Проверяет, считается ли дерево старым (старше 50 лет).

        :return: True, если дерево старше 50 лет, иначе False.

        >>> tree = Tree(60, 15)
        >>> tree.is_old()
        True
        >>> young_tree = Tree(10, 3)
        >>> young_tree.is_old()
        False
        """
        return self.age > 50

# TODO: описать ещё класс
class Book:
    """Класс, описывающий книгу."""
    
    def __init__(self, title: str, pages: int) -> None:
        """
        Инициализирует объект книги.

        :param title: Название книги (не может быть пустым).
        :param pages: Количество страниц (должно быть больше 0).
        :raises ValueError: Если название пустое или страниц 0 и меньше.
        """
        if not title:
            raise ValueError("Название книги не может быть пустым.")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть больше 0.")
        
        self.title = title
        self.pages = pages
        self.current_page = 1  # Книга начинается с первой страницы

    def turn_page(self, pages: int = 1) -> None:
        """
        Перелистывает указанное количество страниц вперед.

        :param pages: Количество страниц для перелистывания (должно быть положительным).
        :raises ValueError: Если указанное число страниц неположительное или выходит за пределы книги.
        
        >>> book = Book("Python Crash Course", 548)
        >>> book.turn_page(10)
        >>> book.current_page
        11
        >>> book.turn_page(290)
        Traceback (most recent call last):
        ...
        ValueError: Нельзя перелистывать за пределы книги.
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным.")
        if self.current_page + pages > self.pages:
            raise ValueError("Нельзя перелистывать за пределы книги.")
        
        self.current_page += pages

    def restart(self) -> None:
        """
        Перелистывает книгу обратно на первую страницу.

        >>> book = Book("Python Guide", 300)
        >>> book.turn_page(50)
        >>> book.restart()
        >>> book.current_page
        1
        """
        self.current_page = 1

# TODO: и ещё один
class Stack:
    """Класс, реализующий стек (LIFO - Last In, First Out)."""
    
    def __init__(self) -> None:
        """Инициализирует пустой стек."""
        self.items = []

    def push(self, item: int) -> None:
        """
        Добавляет элемент в стек.

        :param item: Число, которое нужно добавить в стек.

        >>> stack = Stack()
        >>> stack.push(5)
        >>> stack.items
        [5]
        """
        self.items.append(item)

    def pop(self) -> int:
        """
        Удаляет и возвращает верхний элемент стека.

        :return: Верхний элемент стека.
        :raises IndexError: Если стек пуст.

        >>> stack = Stack()
        >>> stack.push(10)
        >>> stack.pop()
        10
        >>> stack.pop()
        Traceback (most recent call last):
        ...
        IndexError: Стек пуст.
        """
        if not self.items:
            raise IndexError("Стек пуст.")
        return self.items.pop()

    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли стек.

        :return: True, если стек пуст, иначе False.

        >>> stack = Stack()
        >>> stack.is_empty()
        True
        >>> stack.push(1)
        >>> stack.is_empty()
        False
        """
        return len(self.items) == 0

