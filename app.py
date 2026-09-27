import time
import streamlit as st
import pandas as pd
from search_analysis import linear_search, binary_search
from code_benchmark import (
    single_loop,
    nested_loop,
    factorial_recursive,
    factorial_iterative
)
from benchmark_engine import BenchmarkEngine

st.set_page_config(
    page_title="Algorithm Performance Tool",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Algorithm Performance Measurement Tool")

st.write(
    "A benchmarking application for analyzing algorithm "
    "execution time, memory usage, and complexity."
)

st.divider()

st.header("Select Analysis Module")

module = st.selectbox(
    "Choose a module:",
    [
        "Search Algorithm Analysis",
        "Code Benchmarking",
        "Automated Benchmarking",
        "Complexity Analysis"
    ]
)

st.write(f"Selected module: **{module}**")

if module == "Search Algorithm Analysis":

    st.divider()
    st.header("🔎 Search Algorithm Analysis")

    n = st.number_input(
        "Dataset Size",
        min_value=1,
        max_value=50000,
        value=1000,
        step=100
    )

    target = st.number_input(
        "Search Key",
        value=500
    )

    data = list(range(n))

    st.write(f"Dataset contains **{n} sorted elements**.")

    if st.button("Run Search"):
        linear_index, linear_comparisons = linear_search(
            data,
            target
        )

        binary_index, binary_comparisons = binary_search(
            data,
            target
        )

        st.subheader("Linear Search")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Index", linear_index)

        with col2:
            st.metric("Comparisons", linear_comparisons)

        st.subheader("Binary Search")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Index", binary_index)

        with col2:
            st.metric("Comparisons", binary_comparisons)

        st.subheader("Performance Comparison")

        if linear_comparisons < binary_comparisons:
            better = "Linear Search"
        elif binary_comparisons < linear_comparisons:
            better = "Binary Search"
        else:
            better = "Both Equal"

        st.success(f"Better Algorithm: {better}")

elif module == "Code Benchmarking":

    st.header("💻 Code Benchmarking")

    program = st.selectbox(
        "Select Program",
        [
            "Single Loop Traversal",
            "Nested Loop Traversal",
            "Recursive Factorial",
            "Iterative Factorial"
        ]
    )

    input_size = st.number_input(
        "Input Size",
        min_value=1,
        value=100,
        step=100
    )

    st.write("Selected Program:", program)
    st.write("Input Size:", input_size)

    if st.button("Run Benchmark"):

        start_time = time.perf_counter()

        if program == "Single Loop Traversal":
            result = single_loop(input_size)

        elif program == "Nested Loop Traversal":
            result = nested_loop(input_size)

        elif program == "Recursive Factorial":
            result = factorial_recursive(input_size)

        elif program == "Iterative Factorial":
            result = factorial_iterative(input_size)

        end_time = time.perf_counter()

        execution_time = end_time - start_time

        st.success("Benchmark executed successfully!")

        st.subheader("Performance Result")

        st.write("Result:", result)
        st.write("Execution Time:", execution_time, "seconds")

elif module == "Automated Benchmarking":

    st.header("⚙️ Automated Benchmarking")

    st.write(
        "Run multiple algorithms automatically across predefined input sizes."
    )

    benchmark_type = st.selectbox(
        "Select Benchmark Category",
        [
            "Loop Programs",
            "Factorial Programs",
            "Search Algorithms"
        ]
    )

    if st.button("Run Automated Benchmark"):

        engine = BenchmarkEngine()

        if benchmark_type == "Loop Programs":

            sizes = [100, 500, 1000, 2000]

            engine.run(
                single_loop,
                sizes,
                name="Single Loop"
            )

            engine.run(
                nested_loop,
                sizes,
                name="Nested Loop"
            )

        elif benchmark_type == "Factorial Programs":

            sizes = [100, 500, 900]

            engine.run(
                factorial_recursive,
                sizes,
                name="Recursive Factorial"
            )

            engine.run(
                factorial_iterative,
                sizes,
                name="Iterative Factorial"
            )

        elif benchmark_type == "Search Algorithms":

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

        df = engine.as_dataframe()

        st.success("Automated benchmark completed!")

        st.subheader("Benchmark Results")

        st.dataframe(df)

elif module == "Complexity Analysis":

    st.header("📊 Complexity Analysis")

    complexity_data = {
        "Linear Search": {
            "Best Case": "O(1)",
            "Average Case": "O(n)",
            "Worst Case": "O(n)",
            "Space": "O(1)",
            "Growth Trend": "Linear"
        },

        "Binary Search": {
            "Best Case": "O(1)",
            "Average Case": "O(log n)",
            "Worst Case": "O(log n)",
            "Space": "O(1)",
            "Growth Trend": "Logarithmic"
        },

        "Single Loop": {
            "Best Case": "O(n)",
            "Average Case": "O(n)",
            "Worst Case": "O(n)",
            "Space": "O(1)",
            "Growth Trend": "Linear"
        },

        "Nested Loop": {
            "Best Case": "O(n²)",
            "Average Case": "O(n²)",
            "Worst Case": "O(n²)",
            "Space": "O(1)",
            "Growth Trend": "Quadratic"
        },

        "Recursive Factorial": {
            "Best Case": "O(n)",
            "Average Case": "O(n)",
            "Worst Case": "O(n)",
            "Space": "O(n)",
            "Growth Trend": "Linear"
        },

        "Iterative Factorial": {
            "Best Case": "O(n)",
            "Average Case": "O(n)",
            "Worst Case": "O(n)",
            "Space": "O(1)",
            "Growth Trend": "Linear"
        }
    }

    complexity_df = pd.DataFrame(complexity_data).T

    st.dataframe(
        complexity_df,
        use_container_width=True
    )


# ============================================================
# COMPLEXITY ANALYSIS MODULE
# ============================================================

# import pandas as pd
# import streamlit as st


st.header("Complexity Analysis")

st.write(
    "The table below compares the theoretical time and space "
    "complexities of the implemented algorithms and program patterns."
)

complexity_data = {
    "Algorithm / Pattern": [
        "Linear Search",
        "Binary Search",
        "Single Loop",
        "Nested Loop",
        "Recursive Factorial",
        "Iterative Factorial"
    ],
    "Time Complexity": [
        "O(n)",
        "O(log n)",
        "O(n)",
        "O(n²)",
        "O(n)",
        "O(n)"
    ],
    "Space Complexity": [
        "O(1)",
        "O(1)",
        "O(1)",
        "O(1)",
        "O(n)",
        "O(1)"
    ],
    "Observed Growth": [
        "Linear growth",
        "Very slow growth",
        "Linear growth",
        "Quadratic growth",
        "Linear time, higher memory",
        "Linear growth, constant auxiliary space"
    ]
}

complexity_df = pd.DataFrame(complexity_data)

st.dataframe(
    complexity_df,
    use_container_width=True,
    hide_index=True
)

# ============================================================
# EXPERIMENTAL BENCHMARK RESULTS
# ============================================================

st.subheader("Experimental Benchmark Results")

results_file = "results/benchmark_results.csv"

try:
    benchmark_df = pd.read_csv(results_file)

    st.write(
        "The following table contains the experimentally measured "
        "execution time and memory usage for different input sizes."
    )

    st.dataframe(
        benchmark_df,
        use_container_width=True,
        hide_index=True
    )

except FileNotFoundError:
    st.warning(
        "Benchmark results file was not found. "
        "Run benchmark_engine.py first."
    )

# ============================================================
# COMPARATIVE PERFORMANCE STUDY
# ============================================================

st.header("Comparative Performance Study")

st.write(
    "This section compares the experimental performance of the "
    "implemented algorithms and program patterns."
)

# ------------------------------------------------------------
# Search Algorithms
# ------------------------------------------------------------

st.subheader("1. Linear Search vs Binary Search")

st.markdown("""
**Linear Search**

- Time Complexity: O(n)
- Space Complexity: O(1)
- Checks elements sequentially.
- Performance generally increases as the input size increases.

**Binary Search**

- Time Complexity: O(log n)
- Space Complexity: O(1)
- Requires sorted data.
- Repeatedly divides the search interval into two parts.
""")

st.info(
    "Binary Search generally requires fewer comparisons for large "
    "sorted datasets because the search space is reduced by half "
    "after each comparison."
)

# ------------------------------------------------------------
# Factorial Algorithms
# ------------------------------------------------------------

st.subheader("2. Recursive Factorial vs Iterative Factorial")

st.markdown("""
**Recursive Factorial**

- Time Complexity: O(n)
- Space Complexity: O(n)
- Uses recursive function calls.
- Each recursive call adds a new stack frame.

**Iterative Factorial**

- Time Complexity: O(n)
- Space Complexity: O(1)
- Uses a loop and an accumulator.
- Does not require recursive call-stack growth.
""")

st.info(
    "Both implementations perform a linear number of operations, "
    "but Recursive Factorial requires additional call-stack memory."
)

# ------------------------------------------------------------
# Loop Algorithms
# ------------------------------------------------------------

st.subheader("3. Single Loop vs Nested Loop")

st.markdown("""
**Single Loop**

- Time Complexity: O(n)
- Space Complexity: O(1)
- Performs one pass through the input.

**Nested Loop**

- Time Complexity: O(n²)
- Space Complexity: O(1)
- Performs n iterations for each of the n outer-loop iterations.
""")

st.info(
    "The Nested Loop shows substantially faster growth in execution "
    "time as the input size increases because its number of operations "
    "grows quadratically."
)

# ------------------------------------------------------------
# Overall Analysis
# ------------------------------------------------------------

st.subheader("4. Overall Performance Analysis")

st.markdown("""
### Effect of Increasing Input Size

As input size increases, algorithms with higher time complexity
experience a greater increase in execution time.

### Complexity vs Experimental Performance

The benchmark results provide practical measurements that can be
compared with the theoretical complexity of each algorithm.

### Time-Space Trade-Off

Recursive Factorial uses additional memory because of recursive
call-stack growth, while Iterative Factorial uses constant auxiliary
space.

### Scalability

Linear and logarithmic growth patterns generally scale better than
quadratic growth when the input size becomes large.
""")

# ============================================================
# PERFORMANCE VISUALIZATION MODULE
# ============================================================

import matplotlib.pyplot as plt


st.header("Performance Visualizations")

st.write(
    "The following graphs visualize the experimental benchmark "
    "results for execution time and memory usage."
)

# ------------------------------------------------------------
# Load benchmark data
# ------------------------------------------------------------

try:

    # Search algorithms
    search_algorithms = [
        "Linear Search",
        "Binary Search"
    ]

    search_df = benchmark_df[
        benchmark_df["Algorithm"].isin(search_algorithms)
    ]

    # Loop algorithms
    loop_algorithms = [
        "Single Loop",
        "Nested Loop"
    ]

    loop_df = benchmark_df[
        benchmark_df["Algorithm"].isin(loop_algorithms)
    ]

    # Factorial algorithms
    factorial_algorithms = [
        "Recursive Factorial",
        "Iterative Factorial"
    ]

    factorial_df = benchmark_df[
        benchmark_df["Algorithm"].isin(factorial_algorithms)
    ]

    # --------------------------------------------------------
    # Search Algorithm Graph
    # --------------------------------------------------------

    st.subheader("Search Algorithms — Execution Time")

    fig, ax = plt.subplots()

    for algorithm in search_algorithms:

        data = search_df[
            search_df["Algorithm"] == algorithm
        ]

        ax.plot(
            data["Input Size"],
            data["Execution Time (seconds)"],
            marker="o",
            label=algorithm
        )

    ax.set_xlabel("Input Size")
    ax.set_ylabel("Execution Time (seconds)")
    ax.set_title("Linear Search vs Binary Search")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

    # --------------------------------------------------------
    # Loop Graph
    # --------------------------------------------------------

    st.subheader("Loop Programs — Execution Time")

    fig, ax = plt.subplots()

    for algorithm in loop_algorithms:

        data = loop_df[
            loop_df["Algorithm"] == algorithm
        ]

        ax.plot(
            data["Input Size"],
            data["Execution Time (seconds)"],
            marker="o",
            label=algorithm
        )

    ax.set_xlabel("Input Size")
    ax.set_ylabel("Execution Time (seconds)")
    ax.set_title("Single Loop vs Nested Loop")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

    # --------------------------------------------------------
    # Factorial Graph
    # --------------------------------------------------------

    st.subheader("Factorial Programs — Execution Time")

    fig, ax = plt.subplots()

    for algorithm in factorial_algorithms:

        data = factorial_df[
            factorial_df["Algorithm"] == algorithm
        ]

        ax.plot(
            data["Input Size"],
            data["Execution Time (seconds)"],
            marker="o",
            label=algorithm
        )

    ax.set_xlabel("Input Size")
    ax.set_ylabel("Execution Time (seconds)")
    ax.set_title("Recursive vs Iterative Factorial")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

    # --------------------------------------------------------
    # Memory Graph
    # --------------------------------------------------------

    st.subheader("Memory Usage Comparison")

    fig, ax = plt.subplots()

    for algorithm in benchmark_df["Algorithm"].unique():

        data = benchmark_df[
            benchmark_df["Algorithm"] == algorithm
        ]

        ax.plot(
            data["Input Size"],
            data["Memory (KB)"],
            marker="o",
            label=algorithm
        )

    ax.set_xlabel("Input Size")
    ax.set_ylabel("Memory Usage (KB)")
    ax.set_title("Memory Usage Comparison")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

except Exception as e:

    st.error(
        f"Unable to generate visualizations: {e}"
    )