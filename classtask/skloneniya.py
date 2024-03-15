def ruble_declension(number):
    if number % 10 == 1 and number % 100 != 11:
        return "Рубль"
    elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
        return "Рубля"
    else:
        return "Рублей"

number = int(input("Введите целое число: "))
result = ruble_declension(number)
print(f"{number} {result}")