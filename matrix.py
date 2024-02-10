#задаём абстрактный тип number
number = float
#описываем класс "Квадратная матрица"
class Matrix:
    #задаём матрицу по умолчанию - единичная матрица 3х3
    #данные самой матрицы - private, поэтому два нижних подчёркивания перед data
    def __init__(self):
        self.__data = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    #опредяляем метод для того, чтобы получать элемент матрицы через [][]
    def __getitem__(self, item: int):
        return self.__data[item]

    #метод, возвращающий число строк в матрице
    def get_number_of_rows(self):
        return len(self.__data)

    # метод, возвращающий число столбцов в матрице
    def get_number_of_columns(self):
        return len(self.__data[0])
