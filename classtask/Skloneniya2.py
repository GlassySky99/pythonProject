def year_declension(number):
    if number % 10 == 1 and number % 100 != 11:
        return "Год"
    elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
        return "Года"
    else:
        return "Лет"

number = int(input("Введите целое число: "))
result = year_declension(number)
print(f"{number} {result}")