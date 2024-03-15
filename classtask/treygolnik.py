def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# Ввод трех чисел
a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))

if is_triangle(a, b, c):
    print("Можно построить треугольник с заданными сторонами.")
else:
    print("Нельзя построить треугольник с заданными сторонами.")