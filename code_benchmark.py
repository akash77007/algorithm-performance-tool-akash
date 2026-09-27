# ============================================================
# CODE BENCHMARKING MODULE
# ============================================================


# ============================================================
# SINGLE LOOP TRAVERSAL
# ============================================================

def single_loop(n):
    """
    Sums numbers from 0 to n-1 using a single loop.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    total = 0

    for i in range(n):
        total += i

    return total


# ============================================================
# NESTED LOOP TRAVERSAL
# ============================================================

def nested_loop(n):
    """
    Counts all pairs using a nested loop.
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """

    total = 0

    for i in range(n):
        for j in range(n):
            total += 1

    return total


# ============================================================
# RECURSIVE FACTORIAL
# ============================================================

def factorial_recursive(n):
    """
    Calculates n! using recursion.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    if n <= 1:
        return 1

    return n * factorial_recursive(n - 1)


# ============================================================
# ITERATIVE FACTORIAL
# ============================================================

def factorial_iterative(n):
    """
    Calculates n! using iteration.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    result = 1

    for i in range(2, n + 1):
        result *= i

    return result


# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":

    print("Single Loop:")
    print(single_loop(10))

    print("\nNested Loop:")
    print(nested_loop(10))

    print("\nRecursive Factorial:")
    print(factorial_recursive(5))

    print("\nIterative Factorial:")
    print(factorial_iterative(5))