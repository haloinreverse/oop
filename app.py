from matrix import Matrix
#описываем класс "Консольное приложение"
class App:
    def __show_command_menu(self):

        print('Выберите действие и введите его номер:')
        print('1. Ввести новую матрицу.')
        print('2. Рассчитать определитель.')
        print('3. Транспонировать матрицу.')
        print('4. Расчитать ранг матрицы.')
        print('5. Вывести в консоль текущую матрицу.')
        print('6. Выйти из приложения.')

    def execute(self):
        self.__matrix = Matrix()
        self.__show_command_menu()
        n = int(input("Введите число: "))
        while n != 6:
            match n:
                case 1:
                    pass
                    # TODO
                case 2:
                    print(f'Определитель матрицы равен: {self.__matrix.det()}')
                case 3:
                    pass
                    #TODO
                case 4:
                    print(f'Ранг матрицы равен: {self.__matrix.rank()}')
                case 5:
                    self.__matrix.print()
                case 6:
                    break
            self.__show_command_menu()
            n = int(input("Введите число: "))