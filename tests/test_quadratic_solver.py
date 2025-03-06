import unittest
from quadratic_solver import QuadraticEquationSolver

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

if __name__ == '__main__':
    unittest.main()