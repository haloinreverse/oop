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

    #метод получения k-ого минора
    def __get_minor(self, data, k):
        res = []
        for r in data[1:]:
            row = []
            for j in range(len(r)):
                if j != k:
                    row.append(r[j])
            res.append(row)
        return res

    #рекурсивный метод для вычисления определителя матрицы
    def __det_count(self, data):
        n = len(data)
        if n == 2:
            return data[0][0] * data[1][1] - data[0][1] * data[1][0]
        s = 0
        z = 1
        for i in range(n):
            s = s + z * data[0][i] * self.__det_count(self.__get_minor(data, i))
            z = -z
        return s
    #публичный метод для нахождения определителя матрицы
    def get_det(self):
        return self.__det_count(self.__data)
