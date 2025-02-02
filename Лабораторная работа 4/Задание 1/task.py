class ElectronicDevice:
    """
    Базовый класс, представляющий электронное устройство.

    Атрибуты:
        brand (str): Бренд устройства.
        model (str): Модель устройства.
        power (int): Потребляемая мощность в ваттах.
    """

    def __init__(self, brand: str, model: str, power: int) -> None:
        """
        Инициализирует объект электронного устройства.

        Args:
            brand (str): Бренд устройства.
            model (str): Модель устройства.
            power (int): Потребляемая мощность в ваттах.
        """
        self.brand = brand
        self.model = model
        self._power = power  # Закрытый атрибут, так как мощность не должна изменяться напрямую.

    def __str__(self) -> str:
        """Возвращает строковое представление устройства для пользователя."""
        return f"{self.brand} {self.model} ({self._power}W)"

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта для разработчика."""
        return f"ElectronicDevice(brand={self.brand!r}, model={self.model!r}, power={self._power})"

    def turn_on(self) -> None:
        """Включает устройство."""
        print(f"{self.brand} {self.model} включен.")

    def turn_off(self) -> None:
        """Выключает устройство."""
        print(f"{self.brand} {self.model} выключен.")


class Smartphone(ElectronicDevice):
    """
    Класс, представляющий смартфон. Наследуется от ElectronicDevice.

    Дополнительные атрибуты:
        os (str): Операционная система смартфона.
        ram (int): Объем оперативной памяти в ГБ.
    """

    def __init__(self, brand: str, model: str, power: int, os: str, ram: int) -> None:
        """
        Инициализирует объект смартфона, расширяя базовый класс.

        Args:
            brand (str): Бренд смартфона.
            model (str): Модель смартфона.
            power (int): Потребляемая мощность.
            os (str): Операционная система.
            ram (int): Объем оперативной памяти в ГБ.
        """
        super().__init__(brand, model, power)
        self.os = os
        self.ram = ram

    def __str__(self) -> str:
        """Возвращает строковое представление смартфона для пользователя."""
        return f"{self.brand} {self.model} - {self.os}, {self.ram}GB RAM"

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта для разработчика."""
        return f"Smartphone(brand={self.brand!r}, model={self.model!r}, os={self.os!r}, ram={self.ram})"

    def turn_on(self) -> None:
        """
        Перегруженный метод включения смартфона.
        
        В отличие от базового метода, смартфон при включении запускает операционную систему.
        """
        print(f"{self.brand} {self.model} запускается... {self.os} загружается.")

    def install_app(self, app_name: str) -> None:
        """Устанавливает приложение на смартфон."""
        print(f"Приложение {app_name} установлено на {self.brand} {self.model}.")


# Пример использования классов
device = ElectronicDevice("Samsung", "TV-123", 150)
phone = Smartphone("Apple", "iPhone 15", 20, "iOS", 8)

print(device)  # Samsung TV-123 (150W)
print(repr(phone))  # Smartphone(brand='Apple', model='iPhone 15', os='iOS', ram=8)

device.turn_on()  # Samsung TV-123 включен.
phone.turn_on()  # Apple iPhone 15 запускается... iOS загружается.
phone.install_app("Telegram")  # Приложение Telegram установлено на Apple iPhone 15.

