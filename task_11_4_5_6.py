class OfficeStorage:
    def __init__(self, name, count, price):
        self.name = name
        self.count = count
        self.price = price
        self.items = {'name': name, 'count': count, 'price': price}

    def equipment(self):
        try:
            name = input(f'item name: ')
            count = int(input(f'item count: '))
            price = int(input(f'item price: '))
            item = {'name': name, 'count': count, 'price': price}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print('no such stuff!')


class Printer(OfficeStorage):
    pass


class Scanner(OfficeStorage):
    pass


class Xerox(OfficeStorage):
    pass


prntr = Printer('Any Printer', 12, 100)
scnr = Scanner('Any Scanner', 8, 200)
xrx = Xerox('Any Xerox', 200, 16)
prntr.equipment()
scnr.equipment()
xrx.equipment()
