# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# float_num = input('Введите вещественное число: ')

# sum = 0
# for i in float_num:
#     if i != '.':
#         sum += int(i)
# print(sum)


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# n = int(input('Введите число N: '))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     print(factorial, end=' ')


# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = 20
# arr = [pow(1 + 1 / i, n) for i in range(1,n)]
# print(arr)
# print('Sum - ', sum(arr))


# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# 5. Реализуйте алгоритм перемешивания списка.

# import random
# def get_numbers(n):
#     return [i for i in range(-n, n+1)]
# # Read from file
# # f = open("file.txt", "r")
# # positions = list(map(lambda x: int(x.strip("/n"), f.readlines())))
# positions = [0,3,5,6,7,8,4]
# gen_arr = get_numbers(10);
# p = 1
# for pos in positions:
#     p = p * gen_arr[pos]

# print(p)

# print('before shuffle')
# print(gen_arr)
# random.shuffle(gen_arr)
# print('after shuffle')
# print(gen_arr)

