# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# def min_flips(coins):
#     heads = 0
#     tails = 0

#     for coin in coins:
#         if coin == 'H':
#             heads += 1
#         elif coin == 'T':
#             tails += 1

#     return min(heads, tails)


# coins = ['H', 'T', 'H', 'H', 'T', 'T', 'H']
# min_flips_needed = min_flips(coins)
# print(min_flips_needed)




# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две
# подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# def find_numbers(S, P):
#     for x in range(1, 1001):
#         y = S - x
#         if x * y == P:
#             return x, y
    
#     return None


# S = 10
# P = 16
# numbers = find_numbers(S, P)

# if numbers:
#     x, y = numbers
#     print("X =", x)
#     print("Y =", y)
# else:
#     print("Числа не найдены")


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# def powers_of_two(N):
#     power = 0
#     result = 1
#     while result <= N:
#         print(result)
#         power += 1
#         result = 2 ** power


# N = 20
# powers_of_two(N)
