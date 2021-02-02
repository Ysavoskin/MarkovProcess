# MarkovProcess
Coursework from the University program

Необходимо разработать класс «Симулятор марковских процессов» Поля данных – вектор и переходная матрица той же размерности. С помощью методов создаётся марковская последовательность случайных векторов.
Марковский процесс описан следующей формулой: X(k+1) = Ф·X(k) + Г·w(k), где
X(k) ― вектор состояния фазовых координат дискретного сигнала (размерностью n x 1);
Ф ― переходная матрица линейного нестационарного дискретного случайного процесса размерностью n x n;
w(k) ― дискретный стационарный случайный процесс с независимыми значениями, распределённый по заданному закону распределения, размерностью m x 1 (целые n > m > 0);
Г ― матрица размерностью n x m, согласующая размерности X(k) и w(k);
k, k+1 ― дискретные шаги по времени. 
Так как уравнение – разностное, то необходимо начальное условие: X(0) ― вектор размерностью n x 1. В этом случае случайный процесс с независимыми значениями w(k) переходит в винеровский процесс с независимыми приращениями x(k).

Результаты работы:
Введите значение k-1: 
10
Для Винеровского процесса: 
Фи:  8
X:  0
Гамма:  -10
Для Марковского процесса: 
Матрица Фи:  
 [[1.    0.1   0.005]
 [0.    1.    0.1  ]
 [0.    0.    1.   ]]
Вектор X:  
 [[0]
 [0]
 [1]]
Матрица Гамма:  
 [[0]
 [0]
 [1]]
Случайное число w:  9
Результирующий вектор Марковского процесса: 
 [[5.e-03]
 [1.e-01]
 [1.e+01]]
Результат Винеровского процесса:  -90
Случайное число w:  9
Результирующий вектор Марковского процесса: 
 [[ 0.065]
 [ 1.1  ]
 [19.   ]]
Результат Винеровского процесса:  -90
Случайное число w:  4
Результирующий вектор Марковского процесса: 
 [[ 0.27]
 [ 3.  ]
 [23.  ]]
Результат Винеровского процесса:  -40
Случайное число w:  -10
Результирующий вектор Марковского процесса: 
 [[ 0.685]
 [ 5.3  ]
 [13.   ]]
Результат Винеровского процесса:  100
Случайное число w:  8
Результирующий вектор Марковского процесса: 
 [[ 1.28]
 [ 6.6 ]
 [21.  ]]
Результат Винеровского процесса:  -80
Случайное число w:  -10
Результирующий вектор Марковского процесса: 
 [[ 2.045]
 [ 8.7  ]
 [11.   ]]
Результат Винеровского процесса:  100
Случайное число w:  2
Результирующий вектор Марковского процесса: 
 [[ 2.97]
 [ 9.8 ]
 [13.  ]]
Результат Винеровского процесса:  -20
Случайное число w:  8
Результирующий вектор Марковского процесса: 
 [[ 4.015]
 [11.1  ]
 [21.   ]]
Результат Винеровского процесса:  -80
Случайное число w:  9
Результирующий вектор Марковского процесса: 
 [[ 5.23]
 [13.2 ]
 [30.  ]]
Результат Винеровского процесса:  -90
Случайное число w:  2
Результирующий вектор Марковского процесса: 
 [[ 6.7]
 [16.2]
 [32. ]]
Результат Винеровского процесса:  -20
Случайное число w:  -1
Результирующий вектор Марковского процесса: 
 [[ 8.48]
 [19.4 ]
 [31.  ]]
Результат Винеровского процесса:  10

Первая линия Марковского процесса: 
[0, 0.005, 0.065, 0.27, 0.685, 1.2800000000000002, 2.0450000000000004, 2.9700000000000006, 4.015000000000001, 5.230000000000001, 6.700000000000002, 8.480000000000002]

Вторая линия Марковского процесса: 
[0, 0.1, 1.1, 3.0, 5.300000000000001, 6.6000000000000005, 8.700000000000001, 9.8, 11.100000000000001, 13.200000000000001, 16.200000000000003, 19.400000000000002]

Третья линия Марковского процесса: 
[1, 10.0, 19.0, 23.0, 13.0, 21.0, 11.0, 13.0, 21.0, 30.0, 32.0, 31.0]

Винеровский процесс: 
[0, -90, -90, -40, 100, -80, 100, -20, -80, -90, -20, 10]

Случайный сколярный процесс: 
[0, 9, 9, 4, -10, 8, -10, 2, 8, 9, 2, -1]

![screenshot of sample](https://raw.githubusercontent.com/Ysavoskin/MarkovProcess/main/VinerProcess.png)
![screenshot of sample](https://raw.githubusercontent.com/Ysavoskin/MarkovProcess/main/MarkovProcess%201.png)
![screenshot of sample](https://raw.githubusercontent.com/Ysavoskin/MarkovProcess/main/MarkovProcess%202.png)
![screenshot of sample](https://raw.githubusercontent.com/Ysavoskin/MarkovProcess/main/MarkovProcess%203.png)
