import math

class QuadraticEquationSolver:
    @staticmethod
    def solve(a, b, c):
        """Решает квадратное уравнение ax^2 + bx + c = 0."""
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