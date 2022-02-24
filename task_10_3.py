from __future__ import division


class Cell:
    def __init__(self, cells: int):
        self.cells = cells

    def __add__(self, other: 'Cell'):
        return Cell(int(self.cells + other))

    def __sub__(self, other: 'Cell'):
        return Cell(int(self.cells - other))

    def __truediv__(self, other: 'Cell'):
        return Cell(int(self.cells / other))

    def __floor__(self, other: 'Cell'):
        return Cell(int(self.cells // other))

    def __mul__(self, other: 'Cell'):
        return Cell(int(self.cells * other))

    def make_order(self, number: int) -> str:
        all_cells = self.cells // number
        my_list_ = ['*' * number for _ in range(all_cells)]
        my_list_.append('*' * (self.cells % number))
        return '\n'.join(my_list_)


if __name__ == '__main__':
    cell_1 = Cell(15)
    cell_2 = Cell(10)
    cell_3 = Cell(3)

    print(cell_1.make_order(10))

    sum_cell = cell_2 + cell_3
    print(sum_cell.make_order(6))

    mul_cell = cell_2 * cell_3
    print(mul_cell.cells)

    floordiv_cell = cell_2 // cell_3
    print(floordiv_cell.cells)

    truediv_cell = cell_1 / cell_2
    print(truediv_cell.cells)

    try:
        cell_3 - cell_2
    except ValueError as err:
        print(err)

    try:
        cell_1 * 123
    except TypeError as err:
        print(err)
