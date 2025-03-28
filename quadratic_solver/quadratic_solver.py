import math

class QuadraticEquationSolver:
    @staticmethod
    def solve(a, b, c):
        if a == 0:
            if b == 0:
                return None  # Уравнение 0 = c (нет решений или бесконечно много)
            return (-c / b,)  # Линейное уравнение bx + c = 0
        discriminant = b**2 - 4*a*c

        if discriminant < 0:
            return None  # Нет действительных корней
        elif discriminant == 0:
            x = -b / (2*a)
            return (x,)
        else:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            return (x1, x2)
