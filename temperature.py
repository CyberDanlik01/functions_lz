# Функция перевода из градусов Цельсия в Фаренгейты
def C_in_F(celsius):
    return ((celsius * 9/5) + 32)

def main():
    C = float(input("Введите температуру в градусах Цельсия: "))
    F = C_in_F(C)
    print("Температура в градусах Фаренгейта:", F)

if __name__ == "__main__":
    main()
