import math 
#Зададим две функции площади и длины круга(окр-ти)
def circle_area(radius):
    return (math.pi*radius**2)
    #Площадь круга

def circle_lenth(radius):
    return (2* math.pi*radius)  
    #Длина окружности

#Введем радиус с клавиатуры
r = float(input("Введите радиус круга: "))

area = circle_area(r)
lenth = circle_lenth(r)

# Вывод результата
print("Площадь круга:", area)
print("Длина окружности:", lenth)
