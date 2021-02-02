import numpy as np
import matplotlib.pyplot as plt

class Simulator:
    arr = []  # Матрица
    x = []  # Вектор
    line1, line2, line3, line4, line5 = [], [], [], [], []
    print("Введите значение k-1: ")
    k = int(input())

    def __init__(self, n):  # Конструктор класса
        print("Для Винеровского процесса: ")
        self.arrViner = np.random.randint(-10, 10)
        print("Фи: ", self.arrViner)
        self.xViner = 0
        print("X: ", self.xViner)
        self.gViner = np.random.randint(-10, 10)
        print("Гамма: ", self.gViner)
        print("Для Марковского процесса: ")
        self.arr = np.array([[1, 0.1, 0.005], [0, 1, 0.1], [0, 0, 1]])
        print("Матрица Фи: ", self.arr)
        self.x = np.array([[0], [0], [1]])
        print("Вектор X: ", self.x)
        self.g = np.array([[0], [0], [1]])
        print("Матрица Гамма: ", self.g)
        self.w = np.random.randint(-10, 10)
        print("Случайное число w: ", self.w)

    def Process(self):  # Вычисление Марковских и Винеровских процессов
        self.total = self.arr.dot(self.x) + self.g * self.w
        self.totalViner = self.arrViner * self.xViner + self.gViner * self.w
        print("Результирующий вектор Марковского процесса: \n", self.total)
        print("Результат Винеровского процесса: ", self.totalViner)
        self.line1.append(self.x[0][0])
        self.line1.append(self.total[0][0])
        self.line2.append(self.x[1][0])
        self.line2.append(self.total[1][0])
        self.line3.append(self.x[2][0])
        self.line3.append(self.total[2][0])
        self.line4.append(self.xViner)
        self.line4.append(self.totalViner)
        self.line5.append(0)
        self.line5.append(self.w)
        i = 0
        for i in range(self.k):
            self.w = np.random.randint(-10, 10)
            print("Случайное число w: ", self.w)
            self.total = self.arr.dot(self.total) + (self.g * self.w)
            self.totalViner = self.arrViner * self.xViner + self.gViner * self.w
            self.line1.append(self.total[0][0])
            self.line2.append(self.total[1][0])
            self.line3.append(self.total[2][0])
            self.line4.append(self.totalViner)
            self.line5.append(self.w)
            print("Результирующий вектор Марковского процесса: \n", self.total)
            print("Результат Винеровского процесса: ", self.totalViner)
            i += 1

    def PrintLine(self):  # Вывод линий результирующего вектора
        print("\nПервая линия Марковского процесса: ")
        print(self.line1)
        print("\nВторая линия Марковского процесса: ")
        print(self.line2)
        print("\nТретья линия Марковского процесса: ")
        print(self.line3)
        print("\nВинеровский процесс: ")
        print(self.line4)
        print("\nСлучайный сколярный процесс: ")
        print(self.line5)

    def PrintGraph(self):  # Отрисовка графика
        self.x_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        plt.title('Винеровский случайный процесс')
        plt.ylabel('$Изменение$')
        plt.xlabel('$Счетчик k$')
        plt.plot(self.x_arr, self.line4)
        plt.plot(self.x_arr, self.line5)
        plt.show()
        plt.title('Марковский случайный процесс')
        plt.ylabel('$Изменение$')
        plt.xlabel('$Счетчик k$')
        plt.plot(self.x_arr, self.line1)
        plt.show()
        plt.title('Марковский случайный процесс')
        plt.ylabel('$Изменение$')
        plt.xlabel('$Счетчик k$')
        plt.plot(self.x_arr, self.line2)
        plt.show()
        plt.title('Марковский случайный процесс')
        plt.ylabel('$Изменение$')
        plt.xlabel('$Счетчик k$')
        plt.plot(self.x_arr, self.line3)
        plt.show()

# Cоздаем объект класса Симулятор
Obj = Simulator(3)
Obj.Process()
Obj.PrintLine()
Obj.PrintGraph()
