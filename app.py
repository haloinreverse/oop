from matrix import Matrix
#описываем класс "Консольное приложение"
class App:
    def __show_command_menu(self):
        print('Матрица:')
        for i in range(0, self.__matrix.get_number_of_rows()):
            for j in range(0, self.__matrix.get_number_of_columns()):
                print(self.__matrix[i][j], end=' ')
            print('\n')
        print('')
        print('Выберите действие и введите его номер:')
        print('1. Ввести новую матрицу.')
        print('2. Рассчитать определитель.')

    def execute(self):
        self.__matrix = Matrix()
        self.__show_command_menu()
