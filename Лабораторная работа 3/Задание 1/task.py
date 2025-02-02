class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self._name = name  # Используем защищенные атрибуты, так как они не должны изменяться
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Бумажная книга с ограничением на количество страниц."""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Используем свойство для валидации

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, "
                f"pages={self.pages})")


class AudioBook(Book):
    """Аудиокнига с ограничением на продолжительность."""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Используем свойство для валидации

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (float, int)):  # Разрешаем int, так как он совместим с float
            raise TypeError("Продолжительность должна быть числом с плавающей запятой")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = float(value)  # Преобразуем к float для единообразия

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, "
                f"duration={self.duration})")

