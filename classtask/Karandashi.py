def choose_declension(number, word_forms):
    if number % 10 == 1 and number % 100 != 11:
        return word_forms[0]
    elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
        return word_forms[1]
    else:
        return word_forms[2]

number = int(input("Введите целое число: "))
word_forms = [input("Введите слово в именительном падеже: "),
              input("Введите слово в родительном падеже: "),
              input("Введите слово в дательном падеже: ")]

result = choose_declension(number, word_forms)
print(f"{number} {result}")