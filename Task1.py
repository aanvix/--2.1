# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class laptop:
    def __init__(self, cpu: str, ram: int):
        assert isinstance(cpu, str), "CPU должен быть строкой"
        assert isinstance(ram, int), "RAM должен быть целым числом"
        self.cpu = cpu
        self.ram = ram

    def boot_up(self):
        """
        Запускает компьютер.

        :return: None

        Пример:
        >>> lp = laptop("AMD", 16)
        >>> lp.boot_up()
        """
        pass

    def shut_down(self):
        """
        Выключает компьютер.

        :return: None

        Пример:
        >>> lp = laptop("AMD", 16)
        >>> lp.shut_down()
        """
        pass

class Refrigerator:
    def __init__(self, brand: str, capacity: int):
        assert isinstance(brand, str), "Бренд должен быть строкой"
        assert isinstance(capacity, int), "Вместимость должна быть целым числом"
        self.brand = brand
        self.capacity = capacity

    def cool_down(self, temperature: int):
        """
        Охлаждает холодильник до указанной температуры.

        Аргументы:
            temperature (int): Целевая температура.

        :return: None

        Пример:
        >>> fridge = Refrigerator("Samsung", 300)
        >>> fridge.cool_down(5)
        """
        pass
    def defrost(self):
        """
        Размораживает холодильник.

        :return: None

        Пример:
        >>> fridge = Refrigerator("Samsung", 300)
        >>> fridge.defrost()
        """
        pass
class Whatsapp :
    def __init__(self, username: str):
        assert isinstance(username, str), "Имя пользователя должно быть строкой"
        self.username = username

    def send_message(self, recipient: str, message: str):
        """
        Отправляет сообщение указанному получателю.

        Аргументы:
            recipient (str): Получатель сообщения.
            message (str): Сообщение для отправки.

        :return: None

        Пример:
        >>> wa = Whatsapp("Анастасия")
        >>> wa.send_message("Екатерина", "Здравствуй, Анастасия!")
        """
        pass

    def read_message(self, sender: str):
        """
        Читает сообщение от указанного отправителя.

        Аргументы:
            sender (str): Отправитель сообщения.

        :return: None

        Example:
        >>> wa = Whatsapp("Анастасия")
        >>> wa.read_message("Екатерина")
        """
        pass


if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
