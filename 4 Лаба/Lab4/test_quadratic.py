import unittest
import sys
import os

# Добавляем путь к `Lab3`, чтобы импортировать функцию
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Lab3")))

from quadratic_solver import solve_quadratic

class TestQuadraticSolver(unittest.TestCase):
    def test_two_roots(self):
        self.assertEqual(solve_quadratic(1, -3, 2), (2.0, 1.0))

    def test_one_root(self):
        self.assertEqual(solve_quadratic(1, -2, 1), (1.0,))

    def test_no_real_roots(self):
        self.assertEqual(solve_quadratic(1, 1, 1), "Нет действительных корней")

    def test_zero_a(self):
        with self.assertRaises(ValueError):
            solve_quadratic(0, 2, 3)

if __name__ == '__main__':
    unittest.main()
