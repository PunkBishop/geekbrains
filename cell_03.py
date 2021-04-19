class Cell:
    def __init__(self, nums):
        self.nums = nums  # 13

    def make_order(self, rows):  # 5
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return f"{self.nums}"

    def __add__(self, other):
        print("Сумма клеток:")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print("Вычитание клетки:")
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else "Ячеек в первой клетке меньше второй, вычитание невозможно!"

    def __mul__(self, other):
        print("Умножение клетки:")
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print("Floordiv клетки:")
        return Cell(self.nums // other.nums) if other.nums != 0 else "ZeroDivisionError"


cell_1 = Cell(42)
cell_2 = Cell(38)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(7))