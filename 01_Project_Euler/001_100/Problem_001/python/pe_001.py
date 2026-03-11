"""
PROJECT EULER: Problem 1 - Multiples of 3 or 5
---------------------------------------------------------
SOLVED BY: Marzuq Adam & Euler Squad Alpha
DATE: 2026-02-14
STRATEGY: Inclusion-Exclusion Principle (Arithmetic Series)
COMPLEXITY: O(1) Time | O(1) Space
---------------------------------------------------------
Problem: Find the sum of all multiples of 3 or 5 below 1000.
"""

def sum_arithmetic_series(target, divisor):
    """
    Calculates the sum of multiples using the formula:
    Sum = n/2 * (first_term + last_term)
    """
    n = (target - 1) // divisor
    last_term = n * divisor
    return (n * (divisor + last_term)) // 2

def solve():
    target = 1000
    
    # We add multiples of 3 and 5, then subtract 15 
    # to avoid double-counting (Inclusion-Exclusion).
    sum_3 = sum_arithmetic_series(target, 3)
    sum_5 = sum_arithmetic_series(target, 5)
    sum_15 = sum_arithmetic_series(target, 15)
    
    return sum_3 + sum_5 - sum_15

if __name__ == "__main__":
    result = solve()
    print(f"Euler Squad Solution: {result}")