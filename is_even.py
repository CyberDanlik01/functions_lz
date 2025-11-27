def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def main():
    # Введем число с клавиатуры
    a = int(input("Введите число: "))

    if is_even(a):
        print("Четное")
    else:
        print("Нечетное")

if __name__ == "__main__":
    main()
