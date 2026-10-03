# COMPLEXITY ANALYSIS

complexity_data = [
    {
        "Algorithm": "Linear Search",
        "Best Case": "O(1)",
        "Average Case": "O(n)",
        "Worst Case": "O(n)",
        "Space": "O(1)"
    },
    {
        "Algorithm": "Binary Search",
        "Best Case": "O(1)",
        "Average Case": "O(log n)",
        "Worst Case": "O(log n)",
        "Space": "O(1)"
    },
    {
        "Algorithm": "Single Loop",
        "Best Case": "O(n)",
        "Average Case": "O(n)",
        "Worst Case": "O(n)",
        "Space": "O(1)"
    },
    {
        "Algorithm": "Nested Loop",
        "Best Case": "O(n²)",
        "Average Case": "O(n²)",
        "Worst Case": "O(n²)",
        "Space": "O(1)"
    },
    {
        "Algorithm": "Recursive Factorial",
        "Best Case": "O(n)",
        "Average Case": "O(n)",
        "Worst Case": "O(n)",
        "Space": "O(n)"
    },
    {
        "Algorithm": "Iterative Factorial",
        "Best Case": "O(n)",
        "Average Case": "O(n)",
        "Worst Case": "O(n)",
        "Space": "O(1)"
    }
]


def display_complexity_table():

    print("\nComplexity Comparison")
    print("=" * 90)

    print(
        f"{'Algorithm':<25}"
        f"{'Best':<15}"
        f"{'Average':<15}"
        f"{'Worst':<15}"
        f"{'Space':<15}"
    )

    print("-" * 90)

    for item in complexity_data:

        print(
            f"{item['Algorithm']:<25}"
            f"{item['Best Case']:<15}"
            f"{item['Average Case']:<15}"
            f"{item['Worst Case']:<15}"
            f"{item['Space']:<15}"
        )


if __name__ == "__main__":
    display_complexity_table()