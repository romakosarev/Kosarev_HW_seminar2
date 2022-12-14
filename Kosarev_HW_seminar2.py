# 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

#1 вариант решения (работает только с целыми)
# n = input('Введите число: ')
# print(sum(map(int, list(str(n)))))

#2 вариант решения
# n = input('Введите число: ')
# sum = 0
# for i in n:
#     if i.isdigit():
#         sum += int(i)
# print(sum)





# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

#Решение:
# n = int(input('Введите число: '))
#
# a = 1
# for i in range(n):
#     i += 1
#     a = i * a
#
#     print(a, end=', ')






# 3) Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#
# Пример:
#
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# Решение:
# n = int(input('Введите число: '))
# list1 = []
# for i in range(1, n + 1):
#     list1.append((1 +1 / i)**i)
# print(sum(list1))