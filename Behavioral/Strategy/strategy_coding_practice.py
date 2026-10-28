"""
Consider the quadratic equation and its canonical solution:

ax^2 + bx + c = 0
x = (-b ± sqrt(b^2 - 4ac))/2a

The part b^2-4*a*c is called the discriminant. Suppose we want to provide an API with two different strategies for calculating the discriminant:
In OrdinaryDiscriminantStrategy , If the discriminant is negative, we return it as-is. 
This is OK, since our main API returns Complex  numbers anyway.
In RealDiscriminantStrategy , if the discriminant is negative, the return value is NaN (not a number). 
NaN propagates throughout the calculation, so the equation solver gives two NaN values. In Python, you make such a number with float('nan').
Please implement both of these strategies as well as the equation solver itself. 
With regards to plus-minus in the formula, please return the + result as the first element and - as the second. 
Note that the solve() method is expected to return complex values.
"""

from abc import ABC
import cmath

class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        d = b**2 - 4*a *c
        return d

class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        d = b**2 - 4*a *c
        if d <0:
            return float('nan')
        return d


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
         # 1. Calculate discriminant using the injected strategy
        d = self.strategy.calculate_discriminant(a, b, c)

        # 2. Compute the square root (using cmath to support complex outputs)
        sqrt_d = cmath.sqrt(d)
        
        # 3. Apply the quadratic formula variables
        # (Note: if sqrt_d is NaN, Python naturally propagates NaN to both roots)
        root_plus = (-b + sqrt_d) / (2 * a)
        root_minus = (-b - sqrt_d) / (2 * a)
        
        return (root_plus, root_minus)



if __name__ == "__main__":
    # Test case: x^2 - 4x + 13 = 0 (Discriminant is 16 - 52 = -36)
    a, b, c = 1, -4, 13

    # Scenario A: Ordinary strategy yields complex solutions
    ordinary_solver = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())
    roots_ordinary = ordinary_solver.solve(a, b, c)
    print("Ordinary Strategy Roots:")
    print(f"  (+) Root: {roots_ordinary[0]}")
    print(f"  (-) Root: {roots_ordinary[1]}")

    print("-" * 40)

    # Scenario B: Real-only strategy yields NaNs
    real_solver = QuadraticEquationSolver(RealDiscriminantStrategy())
    roots_real = real_solver.solve(a, b, c)
    print("Real Strategy Roots:")
    print(f"  (+) Root: {roots_real[0]}")
    print(f"  (-) Root: {roots_real[1]}")


    # Without complex values
    #2x**2 -10x + 8 =0 
    a, b, c = 2, -10, 8
    real_solver = QuadraticEquationSolver(RealDiscriminantStrategy())
    roots_real = real_solver.solve(a, b, c)
    print("Real Strategy Roots:")
    print(f"  (+) Root: {roots_real[0]}")
    print(f"  (-) Root: {roots_real[1]}")


        