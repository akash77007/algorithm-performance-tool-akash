# ============================================================
# AUTOMATED BENCHMARKING ENGINE
# ============================================================

import time
import tracemalloc
import pandas as pd
from search_analysis import linear_search, binary_search


class BenchmarkEngine:

    def __init__(self):
        self.results = []

    def run(self, func, input_sizes, name=None, arg_builder=lambda n: (n,)):

        algorithm_name = name or func.__name__

        for n in input_sizes:

            args = arg_builder(n)

            # Start memory measurement
            tracemalloc.start()

            # Start time measurement
            start_time = time.perf_counter()

            # Execute function
            func(*args)

            # Stop time measurement
            execution_time = time.perf_counter() - start_time

            # Get peak memory
            current, peak_memory = tracemalloc.get_traced_memory()

            tracemalloc.stop()

            # Store result
            self.results.append({
                "Algorithm": algorithm_name,
                "Input Size": n,
                "Execution Time (seconds)": execution_time,
                "Memory (KB)": peak_memory / 1024
            })

        return self

    def as_dataframe(self):

        return pd.DataFrame(self.results)


# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":

    from code_benchmark import (
        single_loop,
        nested_loop,
        factorial_recursive,
        factorial_iterative
    )

    engine = BenchmarkEngine()

    # Input sizes
    loop_sizes = [100, 500, 1000, 2000]

    factorial_sizes = [100, 500, 900]

    sizes = [100, 500, 1000, 2000]

    engine.run(
        linear_search,
        sizes,
        name="Linear Search",
        arg_builder=lambda n: (list(range(n)), -1)
    )

    engine.run(
        binary_search,
        sizes,
        name="Binary Search",
        arg_builder=lambda n: (list(range(n)), -1)
    )

    # Benchmark loop programs
    engine.run(
        single_loop,
        loop_sizes,
        name="Single Loop"
    )

    engine.run(
        nested_loop,
        loop_sizes,
        name="Nested Loop"
    )

    # Benchmark factorial programs
    engine.run(
        factorial_recursive,
        factorial_sizes,
        name="Recursive Factorial"
    )

    engine.run(
        factorial_iterative,
        factorial_sizes,
        name="Iterative Factorial"
    )

    # Convert results to DataFrame
    results = engine.as_dataframe()

    print("\nBenchmark Results:")
    print(results)

    # Save results
    results.to_csv(
        "results/benchmark_results.csv",
        index=False
    )

    print("\n✓ Results saved to results/benchmark_results.csv")