#Функция перевода времени в секунды
def time_in_sec(hs, min, sec):
    return ((hs * 3600) + (min * 60) + sec)

# Основная функция программы
def main():
    h = int(input("Введите часы: "))
    m = int(input("Введите минуты: "))
    s = int(input("Введите секунды: "))
    
    res = time_in_sec(h, m, s)
    print("В секундах:", res)

if __name__ == "__main__":
    main()


