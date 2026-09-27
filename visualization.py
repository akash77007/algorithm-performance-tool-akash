# ============================================================
# PERFORMANCE VISUALIZATION
# ============================================================

import os

import pandas as pd
import matplotlib.pyplot as plt


RESULTS_FILE = "results/benchmark_results.csv"
GRAPH_DIR = "graphs"


def load_results():
    """Load benchmark results from CSV."""

    return pd.read_csv(RESULTS_FILE)


def create_graph_directory():
    """Create the graphs directory if it does not exist."""

    os.makedirs(GRAPH_DIR, exist_ok=True)


def plot_search_time(df):
    """Compare Linear Search and Binary Search execution time."""

    search_algorithms = [
        "Linear Search",
        "Binary Search"
    ]

    search_df = df[df["Algorithm"].isin(search_algorithms)]

    plt.figure(figsize=(9, 5))

    for algorithm in search_algorithms:

        subset = search_df[
            search_df["Algorithm"] == algorithm
        ]

        plt.plot(
            subset["Input Size"],
            subset["Execution Time (seconds)"],
            marker="o",
            label=algorithm
        )

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Linear Search vs Binary Search")
    plt.legend()
    plt.grid(True)

    plt.savefig(
        f"{GRAPH_DIR}/search_time.png",
        dpi=150,
        bbox_inches="tight"
    )

    plt.close()


def plot_factorial_time(df):
    """Compare Recursive and Iterative Factorial execution time."""

    factorial_algorithms = [
        "Recursive Factorial",
        "Iterative Factorial"
    ]

    factorial_df = df[
        df["Algorithm"].isin(factorial_algorithms)
    ]

    plt.figure(figsize=(9, 5))

    for algorithm in factorial_algorithms:

        subset = factorial_df[
            factorial_df["Algorithm"] == algorithm
        ]

        plt.plot(
            subset["Input Size"],
            subset["Execution Time (seconds)"],
            marker="o",
            label=algorithm
        )

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Recursive Factorial vs Iterative Factorial")
    plt.legend()
    plt.grid(True)

    plt.savefig(
        f"{GRAPH_DIR}/factorial_time.png",
        dpi=150,
        bbox_inches="tight"
    )

    plt.close()


def plot_loop_time(df):
    """Compare Single Loop and Nested Loop execution time."""

    loop_algorithms = [
        "Single Loop",
        "Nested Loop"
    ]

    loop_df = df[
        df["Algorithm"].isin(loop_algorithms)
    ]

    plt.figure(figsize=(9, 5))

    for algorithm in loop_algorithms:

        subset = loop_df[
            loop_df["Algorithm"] == algorithm
        ]

        plt.plot(
            subset["Input Size"],
            subset["Execution Time (seconds)"],
            marker="o",
            label=algorithm
        )

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Single Loop vs Nested Loop")
    plt.legend()
    plt.grid(True)

    plt.savefig(
        f"{GRAPH_DIR}/loop_time.png",
        dpi=150,
        bbox_inches="tight"
    )

    plt.close()


def plot_memory_usage(df):
    """Compare memory usage of all algorithms."""

    plt.figure(figsize=(10, 6))

    for algorithm in df["Algorithm"].unique():

        subset = df[
            df["Algorithm"] == algorithm
        ]

        plt.plot(
            subset["Input Size"],
            subset["Memory (KB)"],
            marker="o",
            label=algorithm
        )

    plt.xlabel("Input Size")
    plt.ylabel("Memory Usage (KB)")
    plt.title("Memory Usage Comparison")
    plt.legend()
    plt.grid(True)

    plt.savefig(
        f"{GRAPH_DIR}/memory_comparison.png",
        dpi=150,
        bbox_inches="tight"
    )

    plt.close()


def generate_all_graphs():

    create_graph_directory()

    df = load_results()

    plot_search_time(df)
    plot_factorial_time(df)
    plot_loop_time(df)
    plot_memory_usage(df)

    print("✓ All graphs generated successfully.")

    print("\nGenerated files:")

    print("1. graphs/search_time.png")
    print("2. graphs/factorial_time.png")
    print("3. graphs/loop_time.png")
    print("4. graphs/memory_comparison.png")


if __name__ == "__main__":
    generate_all_graphs()