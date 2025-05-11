import math


def solve_quadratic(a, b, c):
    """ Решает квадратное уравнение ax^2 + bx + c = 0 """
    if a == 0:
        raise ValueError("Коэффициент 'a' не может быть 0")

    D = b ** 2 - 4 * a * c  # Дискриминант

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return x1, x2
    elif D == 0:
        x = -b / (2 * a)
        return x,
    else:
        return "Нет действительных корней"
