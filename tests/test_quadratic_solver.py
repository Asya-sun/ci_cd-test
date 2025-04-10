import unittest
from quadratic_solver.quadratic_solver import QuadraticEquationSolver

class TestQuadraticEquationSolver(unittest.TestCase):
    def test_no_real_roots(self):
        solver = QuadraticEquationSolver()
        self.assertIsNone(solver.solve(1, 0, 1))  # x^2 + 1 = 0

    def test_one_real_root(self):
        solver = QuadraticEquationSolver()
        roots = solver.solve(1, 2, 1)  # x^2 + 2x + 1 = 0
        self.assertEqual(roots, (-1.0,))

    def test_two_real_roots(self):
        solver = QuadraticEquationSolver()
        roots = solver.solve(1, -3, 2)  # x^2 - 3x + 2 = 0
        self.assertEqual(roots, (2.0, 1.0))

    def test_irrational_roots(self):
        solver = QuadraticEquationSolver()
        delta = 1e-9
        
        # Тест 1: x^2 - 2 = 0 → x = ±√2 ≈ ±1.414213562
        roots = solver.solve(1, 0, -2)
        self.assertIsNotNone(roots)
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], 1.414213562, delta=delta)
        self.assertAlmostEqual(roots[1], -1.414213562, delta=delta)
        
        # Тест 2: x^2 - x - 1 = 0 → x = (1±√5)/2 ≈ 1.618033989 и -0.618033989
        roots = solver.solve(1, -1, -1)
        self.assertIsNotNone(roots)
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], 1.618033989, delta=delta)
        self.assertAlmostEqual(roots[1], -0.618033989, delta=delta)
    
    def test_linear_equation(self):
        """Тест на линейное уравнение (a=0)"""
        # 0x² + 2x - 4 = 0 → x = 2        
        solver = QuadraticEquationSolver()
        delta = 1e-9
        roots = solver.solve(0, 2, -4)
        self.assertAlmostEqual(roots[0], 2.0, delta=delta)

    def test_edge_cases(self):
        """Тест граничных случаев"""
        # x² + 0x + 0 = 0 → x = 0
        solver = QuadraticEquationSolver()
        roots = solver.solve(1, 0, 0)
        self.assertEqual(roots, (0.0,))

    def test_edge_cases_2(self):
        """Тест граничных случаев"""
        # x² + 0x + 0 = 1 → x = +-1
        solver = QuadraticEquationSolver()
        roots = solver.solve(1, 0, -1)
        self.assertEqual(roots, (1.0, -1.0))

    def test_edge_cases_3(self):
        # 0x² + 0x + 0 = 0 → бесконечно много решений (но наш метод вернет None)
        solver = QuadraticEquationSolver()
        self.assertIsNone(solver.solve(0, 0, 0))
        

if __name__ == '__main__':
    unittest.main()