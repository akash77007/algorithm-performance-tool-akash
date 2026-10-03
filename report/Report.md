
# 1. Introduction

The objective of this lab is to develop a Python-based tool for measuring and comparing the performance of different algorithms.

The project measures:

- Execution time
- Memory usage
- Number of comparisons/operations
- Performance for different input sizes

The implemented algorithms include Linear Search, Binary Search, Single Loop, Nested Loop, Recursive Factorial, and Iterative Factorial.

---

# 2. Question 1 — Project Setup

The project workspace was created using Python, a virtual environment, required libraries, Git, and GitHub.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Streamlit | Interactive web application |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Matplotlib | Graph generation |
| Tracemalloc | Memory measurement |
| Jupyter Notebook | Experimental analysis |
| Git/GitHub | Version control |

## Project Structure

```text
daa_lab2/
│
├── app.py
├── search_analysis.py
├── code_benchmark.py
├── benchmark_engine.py
├── complexity_analysis.py
├── visualization.py
├── project_notebook.ipynb
├── requirements.txt
├── README.md
│
├── graphs/
│   ├── search_time.png
│   ├── factorial_time.png
│   ├── loop_time.png
│   └── memory_comparison.png
│
└── results/
    └── benchmark_results.csv
```

### Screenshot — Project Setup

> ![[Pasted image 20261003152620.png|269]]
>
> 

### Screenshot — GitHub Repository

>![[Pasted image 20261003152722.png|577]]
>
>

---

# 3. Question 2 — Linear Search and Binary Search

Linear Search checks elements sequentially until the target is found.

Binary Search repeatedly divides a sorted dataset into two halves to locate the target.

## Linear Search

### Code

```python
def linear_search(arr, target):
    comparisons = 0
    for i, value in enumerate(arr):
        comparisons += 1
        if value == target:
            return i, comparisons
    return -1, comparisons
```

### Binary Search

### Code

```python
def binary_search(arr, target):

    low = 0
    high = len(arr) - 1
    result = -1
    comparisons = 0
    
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result, comparisons
```

### Complexity

| Algorithm | Best Case | Average Case | Worst Case | Space |
|---|---|---|---|---|
| Linear Search | O(1) | O(n) | O(n) | O(1) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |

### Search Output

> ![[Pasted image 20261003153307.png|556]]
>

### Search Performance

>![[Pasted image 20261003153339.png|592]]

---

# 4. Question 3 — Code Benchmarking Module

The Code Benchmarking Module was developed to execute and compare the following programs:

1. Single Loop Traversal
2. Nested Loop Traversal
3. Recursive Factorial
4. Iterative Factorial

## Code

```python
# CODE BENCHMARKING MODULE

def single_loop(n):
    total = 0
    for i in range(n):
        total += i
    return total

def nested_loop(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += 1
    return total

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# TESTING

if __name__ == "__main__":

    print("Single Loop:")
    print(single_loop(10))

    print("\nNested Loop:")
    print(nested_loop(10))

    print("\nRecursive Factorial:")
    print(factorial_recursive(5))

    print("\nIterative Factorial:")
    print(factorial_iterative(5))
```

## Complexity

| Program | Time Complexity | Space Complexity |
|---|---|---|
| Single Loop | O(n) | O(1) |
| Nested Loop | O(n²) | O(1) |
| Recursive Factorial | O(n) | O(n) |
| Iterative Factorial | O(n) | O(1) |

### Benchmark Output

>![[Pasted image 20261003153739.png|418]]


>![[Pasted image 20261003153824.png]]

---

# 5. Question 4 — Automated Benchmarking Engine

An automated benchmarking engine was implemented to execute algorithms for different input sizes and record their performance.

The engine records:

- Algorithm name
- Input size
- Execution time
- Memory usage

## Code

```python
class BenchmarkEngine:
    def __init__(self):
        self.results = []
        
    def run(self, func, input_sizes, name=None, arg_builder=lambda n: (n,)):
        algorithm_name = name or func.__name__
        
        for n in input_sizes:
            args = arg_builder(n)

            tracemalloc.start()
            start_time = time.perf_counter()
            func(*args)
            execution_time = time.perf_counter() - start_time
            current, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            self.results.append({
                "Algorithm": algorithm_name,
                "Input Size": n,
                "Execution Time (seconds)": execution_time,
                "Memory (KB)": peak_memory / 1024
            })
        return self
    def as_dataframe(self):
        return pd.DataFrame(self.results)
```

The collected results are stored in:

```text
results/benchmark_results.csv
```

### Benchmark Results

>![[Pasted image 20261003154148.png|638]]


---

# 6. Question 5 — Complexity Comparison

The theoretical complexity of all implemented algorithms was compared using the following table.

| Algorithm | Best Case | Average Case | Worst Case | Space |
|---|---|---|---|---|
| Linear Search | O(1) | O(n) | O(n) | O(1) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |
| Single Loop | O(n) | O(n) | O(n) | O(1) |
| Nested Loop | O(n²) | O(n²) | O(n²) | O(1) |
| Recursive Factorial | O(n) | O(n) | O(n) | O(n) |
| Iterative Factorial | O(n) | O(n) | O(n) | O(1) |

## Complexity Analysis Code

```python
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
```

### Observed Performance

> ![[Pasted image 20261003154629.png|665]]


---

# 7. Question 6 — Visualizations and Performance Observations

Performance graphs were generated using Matplotlib to compare the implemented algorithms.

## 7.1 Search Algorithm Comparison

The graph compares the execution time of Linear Search and Binary Search for different input sizes.

> ![[Pasted image 20261003154656.png]]

---

## 7.2 Factorial Comparison

The graph compares Recursive Factorial and Iterative Factorial.

>![[Pasted image 20261003154706.png]]

---

## 7.3 Loop Comparison

The graph compares Single Loop and Nested Loop performance.

>![[Pasted image 20261003154716.png]]

---

## 7.4 Memory Comparison

The graph compares the memory usage of the implemented algorithms.

> ![[Pasted image 20261003154728.png]]

---

## Performance Observations

- Linear Search checks elements sequentially.
- Binary Search reduces the search space by half at every step.
- Single Loop has linear growth with input size.
- Nested Loop has quadratic growth and becomes significantly slower for larger inputs.
- Recursive Factorial uses additional call-stack memory.
- Iterative Factorial uses constant auxiliary space.

---

# 8. Question 7 — Benchmarking Report and Analysis

The complete benchmarking analysis combines theoretical complexity with experimental measurements.

## Search Analysis

Linear Search performs sequential comparisons, while Binary Search repeatedly divides the sorted search space.

> ![[Pasted image 20261003154953.png|567]]

## Factorial Analysis

Both Recursive and Iterative Factorial have O(n) time complexity. However, the recursive implementation requires additional stack space, while the iterative implementation uses constant auxiliary space.

> ![[Pasted image 20261003155020.png|515]]

## Loop Analysis

Single Loop performs a linear number of operations, while Nested Loop performs approximately n² operations.

> ![[Pasted image 20261003155218.png|325]]
> 
> ![[Pasted image 20261003155239.png|324]]

## Time-Space Trade-Off

The project demonstrates that algorithm selection depends on both time and space requirements.

Binary Search provides logarithmic search time but requires sorted data.

Recursive Factorial and Iterative Factorial have the same asymptotic time complexity but differ in auxiliary space usage.

---

# 9. Streamlit Application

A Streamlit application was developed to provide an interactive interface for the performance measurement tool.

The application allows users to:

- Select an analysis module
- Enter input sizes
- Run algorithms
- View results
- Compare performance

### Application Screenshot

> ![[Pasted image 20261003155320.png]]

---

# 10. Conclusion

The Algorithm Performance Measurement and Benchmarking Tool demonstrates the relationship between theoretical algorithmic complexity and practical performance.

The project combines:

- Algorithm implementation
- Performance measurement
- Memory analysis
- Complexity analysis
- Automated benchmarking
- Data collection
- Visualization
- Streamlit interface

The experiments demonstrate how increasing input size affects algorithm execution time and memory usage.

---

# 12. Repository

The complete project source code, graphs, benchmark results, notebook, and documentation are maintained in the GitHub repository.

> **[akash77007/algorithm-performance-tool-akash](https://github.com/akash77007/algorithm-performance-tool-akash)**
