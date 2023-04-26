import time
import numpy
import random
import matplotlib.pyplot as plt
from Funcs import *
from Generation import method_smirnov_transform, method_middle_products
'''
1. Модифицировать (предложить собственные) два метода генерации псевдослучайных чисел.
2. Получить не менее 10 выборок каждым методом 
   (диапазон чисел в каждой выборке не менее 10000) объемом не менее 50 элементов каждая.
3. Для каждой выборки посчитать среднее, отклонение и коэффициент вариации. Сделать вывод об однородности выборки.
4. Каждую выборку проверить на равномерность распределения и случайность, используя критерий Хи-квадрат.
5. Засечь время генерации чисел от тысячи до миллиона элементов обоими предложенными методами 
   и любым стандартным методом используемого языка программирования. 
   Построить графики сравнения скоростей в зависимости от объема выборки.
'''



rand_sizes = [50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]

print("Линейный конгруэнтный метод:")
for i in rand_sizes:
    gen_params(method_smirnov_transform(i))

print("Метод серединных произведений:")
for i in rand_sizes:
    gen_params(method_middle_products(i))

smirnov_transform_time = []
middle_products_time = []
std_time = []

rand_sizes = [1000, 2500, 5000, 7500, 10000, 25000, 50000, 75000, 100000, 250000, 500000, 750000, 1000000]
for g in rand_sizes:
    time_start = time.time()
    method_smirnov_transform(g)
    smirnov_transform_time.append(round(time.time() - time_start, 6))

    time_start = time.time()
    method_middle_products(g)
    middle_products_time.append(round(time.time() - time_start, 6))

    time_start = time.time()
    numpy.random.random_integers(1, 10000, g)  # Стандартный метод генерации чисел
    std_time.append(round(time.time() - time_start, 6))

print("Время генерации:")
print("\tЛинейный конгруэнтный метод:", smirnov_transform_time)
print("\tМетод серединных произведений:", middle_products_time)
print("\tСтандартный способ:", std_time)
x1 = [i * 100 for i in smirnov_transform_time]
x2 = [i*100 for i in middle_products_time]
x3 = [i*100 for i in std_time]

plt.style.use('ggplot')
plt.title('График времени сортировки')
plt.ylabel('Время умноженное на 100', color='gray')
plt.text(0.01, 100, 'Red line - simple search')
#plt.text(0.01, 0.105, '- simple search')

plt.text(0.01, 150, 'Green line - binary search')
#plt.text(0.01, 0.09, '- binary search')

plt.text(0.01, 200, 'Blue line - binary sort search')
#plt.text(0.01, 0.08, '- binary sort search')
x = [i/10 for i in range(len(rand_sizes))]
plt.plot(x, x1, 'r-', x, x2, 'g-', x, x3, 'b-')
plt.show()
