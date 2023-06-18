#  Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)
    
print("Введите число: ")
number = int(input())
    
print("Сумма цифр в числе", number, "равна", sum_of_digits(number))


