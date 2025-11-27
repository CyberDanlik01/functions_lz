import math 
#Зададим две функции площади и длины круга(окр-ти)
def circle_area(radius):
    return (math.pi*radius**2)
    #Площадь круга

def circle_length(radius):
    return (2* math.pi*radius)  
    #Длина окружности

def main():
    r = float(input("Введите радиус круга: "))
    area = circle_area(r)
    length = circle_length(r)

    #Выведем
    print("Площадь круга:", area)
    print("Длина окружности:", length)

if __name__ == "__main__":
    main()

