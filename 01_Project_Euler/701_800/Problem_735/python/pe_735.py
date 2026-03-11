\"\"\"
# Python code for Problem 735
**Date**: October 10, 2024

Let \(n)\$ be the number of divisors of \^2\$ that are no greater than n.
For example, \(15)=8\$ because there are 8 such divisors: 1, 2, 3, 5, 6, 9, 10, 15.

Let:
\$\(N)=\sum_{n=1}^{N}f(n)\$\$

Target: Find \(10^{12})\$
\"\"\"

def f(n):
    \"\"\"
    This function loops through integers 1 to n and checks for which integers 
    divide 2n^2 cleanly, stores them in a list and counts them.
    \"\"\"
    res = [i for i in range(1, n + 1) if (2 * n**2) % i == 0] #
    return len(res) #

def F(N):
    \"\"\"
    Loops through integers n=1 to N and applies f(n) to each, then sums the result.
    \"\"\"
    res_2 = [f(j) for j in range(1, N + 1)] #
    return sum(res_2) #

if __name__ == "__main__":
    # Results verified in 2024
    print(f"F(10^4) = {F(10**4)}") # Expected Output: 242226
