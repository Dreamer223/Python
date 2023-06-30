# N = "a a a b c a a d c d d".split()
# count=0
# for i in range(len(N)):
#     for j in range(i+1len(N)):
#         if N[i]==N[j]:
#             count +=1
#             N[j] += "_"+str(count)
#     coint = 0

# print(N)


# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов 
# идущих подряд слова разделены одним пробелом. Определите сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells 
# I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 13

# N=("She sells sea shells on the sea shore The shells that she sells are sea shells Im sure So if she sells sea shells on the sea shore Im sure that the shells are sea shore shells").upper().split()
# print (N)

# print (len(set(N)))

# 3.

# N=[]
# x = int(input())
# N.append(x)
# while x != 0:
#     x = int(input())
#     N.append(x)
# N.pop()
# print(N)


# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. 
# Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем 
# (число 0 не входит в последовательность)”. Однако 2  друга оказались не такими смышлеными. Никто из ребят не смог до конца 
# сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.

# Ваня:

# n = int(input())
# max_number = 1000
# while n != 0:
#    n = int(input())
#    if max_number > n:
#        max_number = n
# print(max_number)


# Петя:

# n = int(input())
# max_number = -1
# while n < 0:
#    n = int(input())
#    if max_number < n:
#        n = max_number
# print(n)


# Задача №112515. Построчный редактор
# Напишите программу, которая управляет текстовым редактором по командам, записанным в файл output.txt . 
# Строки текста нумеруются с единицы. Сначала список строк пустой. Существует три команды: '+' – добавление строки, '-' – 
# удаление строки и '*' – замена строки. Попытка удалить или заменить строку, которой нет в списке, считается ошибкой. Ошибочна 
# также и вставка строки с номером, который более чем на единицу превышает количество строк в тексте.

# Входные данные
# В файле input.txt записаны строки с командами, последняя строка файла – пустая. Первый символ любой рабочей строки – это команда 
# ('+', '-' или '*'), далее без пробела записывается номер строки, а затем (для команд '+' и '*') – текст новой строки, который нужно 
# добавить или заменить.

# Выходные данные
# Программа должна вывести в файл output.txt все строки, которые остались в списке после обработки всех команд. 
# Если в списке не осталось ни одной строки, нужно вывести слово 'EMPTY'. Если произошла ошибка, нужно вывести слово 'ERROR'.

# Примеры
# входные данные
# +1 I am a pupil.
# +2 He is a pupil.
# +2 She is a pupil.
# +3 This is a pupil.
# *2 Bob went home.
# -3
# выходные данные
# I am a pupil.
# Bob went home.
# He is a pupil.
text=()
operation=str(input())
if(operation == "+"):
    
    text=
elif (operation == "-"):

elif(operation=="*")



