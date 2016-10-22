"""Tests for Van der Pol Oscillator

This script has tests for Van der Pol Oscillator solve function from
van_der_pol.py

How to Use?
-----------
python3 tests.py
"""


from van_der_pol import solve
import unittest


class TestVanDerPol(unittest.TestCase):
    def test_initial_condition(self):
        """Tests that the initial solution follows from the specified initial
        condition."""
        [x, y, t] = solve([0, 0], tstart=0, tend=20, tnum=100)
        self.assertAlmostEqual(x[0], 0.0)
        self.assertAlmostEqual(y[1], 0.0)

    def test_solution_zero_initial_conditions(self):
        """Tests that for zero initial conditions, the solution remains zero
        for all times."""
        [x, y, t] = solve([0, 0], tstart=0, tend=20, tnum=100)
        for i in range(100):
            self.assertAlmostEqual(x[i], 0.0)
            self.assertAlmostEqual(y[i], 0.0)

if __name__ == '__main__':
    unittest.main()
