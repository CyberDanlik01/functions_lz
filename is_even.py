#Напишем ф-ию для проверки четности числа
def is_even(number):
    if number %2 == 0:
        return True
    else:
        return False

#Введем число с клавиатуры
a = int(input("Введите число: "))

if is_even(a):
    print("Четное")
else:
    print("Нечетное")
    