# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько 
# легко он их придумывает, Вам стоит написать программу. Винни-Пух считает,
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе 
# стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе 
# несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  


# def count_vowels(word):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in word:
#         if char in vowels:
#             count += 1
#     return count

# def check_rhythm(poem):
#     phrases = poem.split()
#     vowel_counts = []

#     for phrase in phrases:
#         words = phrase.split("-")
#         phrase_vowel_count = sum(count_vowels(word) for word in words)
#         vowel_counts.append(phrase_vowel_count)

#     if len(set(vowel_counts)) == 1:
#         return "Парам пам-пам"
#     else:
#         return "Пам парам"

# # Считываем стихотворение
# poem = input()

# # Проверяем ритм
# result = check_rhythm(poem)

# # Выводим результат
# print(result)



# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть 
# распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,
# как, например, у операции умножения.
# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**

# 1 2 3 4 5 62 4 6 8 10 123 6 9 12 15 184 8 12 16 20 245 10 15 20 25 306 12 18 24 30 36

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        row = []
        for j in range(1, num_columns + 1):
            element = operation(i, j)
            row.append(str(element))
        print(" ".join(row))

# Пример использования функции
print_operation_table(lambda x, y: x * y)
