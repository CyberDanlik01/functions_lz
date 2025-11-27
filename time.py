def time_in_sec(hs, min, sec):
    return ((hs*3600) + (min*60) + sec)

#Введем данные с клавиатуры
h = int(input("Введите часы: "))
m = int(input("Введите минуты: "))
s = int(input("Введите секунды: "))

#Переведем в секунды
res = time_in_sec(h, m, s)

#Результат
print("В секундах:", res)
