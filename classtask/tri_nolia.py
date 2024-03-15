numbers = []
zero_count = 0

while zero_count < 3:
    num = float(input("Введите число (для завершения введите 0): "))

    if num == 0:
        zero_count += 1
        continue

    numbers.append(num)

if numbers:
    average = sum(numbers) / len(numbers)
    print(f"Среднее арифметическое введенных чисел без учета нулей: {average}")
else:
    print("Не было введено ни одного числа, нельзя посчитать среднее.")