"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП.
"""

from abc import ABC, abstractmethod


class StockError(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquipmentStock:
    def __init__(self):
        self._equipment = []
        self._equipment_in_units = dict({})

    def put(self, equipment, count):
        self.validate_count(count)
        if not isinstance(equipment, OfficeEquipment):
            raise StockError('Stock accepts only office equipment')
        self._equipment.append(equipment)

    def move_to_unit(self, unit_name, count, equipment_type):
        self.validate_count(count)
        self._equipment_in_units.setdefault(unit_name, [])
        self._equipment_in_units[unit_name].extend([self._equipment.pop() for _ in self._equipment[0:count]])

    @staticmethod
    def validate_equipment_type(equipment_type):
        if type(equipment_type) is not OfficeEquipment:
            raise StockError('This stock works only with office equipment')

    @staticmethod
    def validate_count(count):
        if type(count) is not int:
            try:
                return int(count)
            except ValueError:
                raise StockError('Count should be a number')

    @staticmethod
    def validate_unit(unit):
        if type(unit) is not str:
            raise StockError('Unit should be a string')
        if not len(unit) > 0:
            raise StockError('Unit should be a non-empty string')


class OfficeEquipment(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def inventory_number(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, name, inventory_number, sheets_count):
        super().__init__()
        self._name = name
        self._inventory_number = inventory_number
        self._sheets_count = sheets_count

    @property
    def name(self):
        return self._name

    @property
    def inventory_number(self):
        return self._inventory_number

    @property
    def sheets_count(self):
        return self._sheets_count


class Scanner(OfficeEquipment):
    def __init__(self, name, inventory_number, resolution):
        super().__init__()
        self._name = name
        self._inventory_number = inventory_number
        self._resolution = resolution

    @property
    def name(self):
        return self._name

    @property
    def inventory_number(self):
        return self._inventory_number

    @property
    def resolution(self):
        return self._resolution


class Copier(OfficeEquipment):
    def __init__(self, name, inventory_number, coloured):
        super().__init__()
        self._name = name
        self._inventory_number = inventory_number
        self._coloured = coloured

    @property
    def name(self):
        return self._name

    @property
    def inventory_number(self):
        return self._inventory_number

    @property
    def is_coloured(self):
        return self._coloured


def put_printers_to_stock(stock):
    while True:
        try:
            s = input('How many printers do you want put to stock? ')
            stock.put(Printer(name='The Printer', inventory_number=123, sheets_count=300), s)
            break
        except StockError as e:
            print(e.txt)


def put_scanners_to_stock(stock):
    while True:
        try:
            s = input('How many scanners do you want put to stock? ')
            stock.put(Scanner(name='The Scanner', inventory_number=456, resolution=300), s)
            break
        except StockError as e:
            print(e.txt)


def put_copiers_to_stock(stock):
    while True:
        try:
            s = input('How many copiers do you want put to stock? ')
            stock.put(Copier(name='The Copier', inventory_number=123, coloured=True), s)
            break
        except StockError as e:
            print(e.txt)


def move_printers_to_unit(stock):
    while True:
        try:
            s = input('In which unit do you want move printers? ')
            stock.put(Printer(name='The Printer', inventory_number=123, sheets_count=300), s)
            break
        except StockError as e:
            print(e.txt)


if __name__ == '__main__':
    office_stock = OfficeEquipmentStock()
    # office_stock.put({'name': 'Failing printer'}, 5)
    put_printers_to_stock(office_stock)
    put_scanners_to_stock(office_stock)
    put_copiers_to_stock(office_stock)
    move_printers_to_unit(office_stock)

