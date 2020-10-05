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
from copy import deepcopy


class StockError(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquipmentStock:
    def __init__(self):
        self._equipment = []
        self._equipment_in_units = dict({})

    def put(self, equipment, count):
        self.validate_equipment_type(type(equipment))
        quantity = self.validate_and_parse_count(count)
        if not isinstance(equipment, OfficeEquipment):
            raise StockError('Stock accepts only office equipment')
        for _ in range(quantity):
            self._equipment.append(deepcopy(equipment))

    def move_to_unit(self, unit_name, count, equipment_type):
        quantity = self.validate_and_parse_count(count)
        self.validate_equipment_type(equipment_type)
        self._equipment_in_units.setdefault(unit_name, [])
        items = [item for item in self._equipment if type(item) == equipment_type][:quantity]
        if len(items) < quantity:
            raise StockError(f'You do not have {quantity} of equipment')
        for item in items:
            self._equipment.remove(item)
        self._equipment_in_units[unit_name].extend(items)

    def count_equipment_by_type(self, equipment_type):
        return len([item for item in self._equipment if type(item) == equipment_type])

    @staticmethod
    def validate_equipment_type(equipment_type):
        if not issubclass(equipment_type, OfficeEquipment):
            raise StockError('This stock works only with office equipment')

    @staticmethod
    def validate_and_parse_count(count):
        if type(count) is not int:
            try:
                return int(count)
            except ValueError:
                raise StockError('Count should be a number')
        return count

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
            unit = input('In which unit do you want move printers? ')
            count = input('How many printers do you want to move? ')
            stock.move_to_unit(unit, count, Printer)
            break
        except StockError as e:
            print(e.txt)


if __name__ == '__main__':
    office_stock = OfficeEquipmentStock()
    # office_stock.put({'name': 'Failing printer'}, 5)
    put_printers_to_stock(office_stock)
    put_scanners_to_stock(office_stock)
    put_copiers_to_stock(office_stock)
    print(f'We have {office_stock.count_equipment_by_type(Printer)} printers')
    print(f'We have {office_stock.count_equipment_by_type(Scanner)} scanners')
    print(f'We have {office_stock.count_equipment_by_type(Copier)} copiers')
    move_printers_to_unit(office_stock)
    print(f'We have {office_stock.count_equipment_by_type(Printer)} printers')

