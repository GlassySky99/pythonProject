numbers = []
while True:
    num = float(input("Введите число (для завершения введите 0): "))

    if num == 0:
        break

    numbers.append(num)

if numbers:
    average = sum(numbers) / len(numbers)
    print(f"Среднее арифметическое введенных чисел: {average}")
else:
    print("Не было введено ни одного числа, нельзя посчитать среднее.")
