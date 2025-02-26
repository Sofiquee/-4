class Fruit:
    def __init__(self, name: str, color: str, weight: float) -> None:
        """
        Инициализация базового класса Fruit.
        :param name: Название фрукта
        :param color: Цвет фрукта
        :param weight: Вес фрукта в граммах
        """
        self._name = name  # Приватный атрибут (начинается с _, так как это внутренний)
        self._color = color
        self._weight = weight

    def get_info(self) -> str:
        """
        Возвращает информацию о фрукте.
        :return: Строка с информацией о фрукте
        """
        return f"{self._name} - {self._color}, вес: {self._weight} г"

    def __str__(self) -> str:
        """
        Возвращает строковое представление фрукта.
        :return: Строчка с названием фрукта и его цветом
        """
        return f"{self._name} ({self._color})"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление фрукта.
        :return: Форматированная строка для представления объекта Fruit
        """
        return f"Fruit(name='{self._name}', color='{self._color}', weight={self._weight})"

class Apple(Fruit):
    def __init__(self, variety: str, color: str, weight: float) -> None:
        """
        Инициализация дочернего класса Apple.
        :param variety: Сорт яблока
        :param color: Цвет яблока
        :param weight: Вес яблока в граммах
        """
        super().__init__(name="Яблоко", color=color, weight=weight)
        self.variety = variety  # Публичный атрибут

    def get_info(self) -> str:
        """
        Возвращает информацию о яблоке, включая его сорт.
        Переопределение метода get_info, чтобы предоставить больше информации о яблоке.
        :return: Строка с информацией о яблоке
        """
        return f"{super().get_info()}, сорт: {self.variety}"

    def __str__(self) -> str:
        """
        Возвращает строковое представление яблока с указанием сорта.
        :return: Строка с названием и сортом яблока
        """
        return f"{self.variety} Яблоко ({self._color})"

class Orange(Fruit):
    def __init__(self, color: str, weight: float) -> None:
        """
        Инициализация дочернего класса Orange.
        :param color: Цвет апельсина
        :param weight: Вес апельсина в граммах
        """
        super().__init__(name="Апельсин", color=color, weight=weight)

    def __str__(self) -> str:
        """
        Возвращает строковое представление апельсина.
        :return: Строка с названием апельсина и его цветом
        """
        return f"Апельсин ({self._color})"

if __name__ == "__main__":
    apple = Apple(variety="Грени Смит", color="Зеленый", weight=150.0)
    orange = Orange(color="Оранжевый", weight=200.0)

    print(apple.get_info())
    print(orange.get_info())
    print(str(apple))
    print(repr(apple))
    print(str(orange))
    print(repr(orange))