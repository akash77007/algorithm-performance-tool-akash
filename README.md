# Algorithm Performance Measurement and Benchmarking Tool

## Lab Assignment 2

A Python-based Algorithm Performance Measurement and Benchmarking Tool developed as part of the Design and Analysis of Algorithms Lab.

---

## Student Information

| Field | Details |
|---|---|
| Name | Akash Sharma |
| Roll Number | 2401201108 |
| Program | BCA (AI & DS) |
| Section | B |
| Semester | V |
| Course | Design and Analysis of Algorithms Lab |
| Course Code | ENCA351 |
| Faculty | Dr. Aarti |
| Session | 2026-27 |
| University | K.R. Mangalam University |

---

# 1. Project Overview

The Algorithm Performance Measurement and Benchmarking Tool is designed to measure and compare the practical performance of different algorithms and programming patterns.

The project measures:

- Execution time
- Memory usage
- Number of comparisons where applicable
- Performance growth with increasing input size
- Theoretical time complexity
- Theoretical space complexity

The project also generates graphical visualizations to make performance trends easier to understand.

---

# 2. Algorithms and Programs Implemented

## Search Algorithms

### Linear Search

Linear Search checks elements sequentially from left to right until the target is found or the complete array has been searched.

Time Complexity:

- Best Case: O(1)
- Average Case: O(n)
- Worst Case: O(n)

Space Complexity:

- O(1)

### Binary Search

Binary Search repeatedly divides a sorted search interval into two halves.

Time Complexity:

- Best Case: O(1)
- Average Case: O(log n)
- Worst Case: O(log n)

Space Complexity:

- O(1) for the iterative implementation

---

## Code Benchmarking Programs

### Single Loop Traversal

A single loop traverses the input once.

Time Complexity:

- O(n)

Space Complexity:

- O(1)

### Nested Loop Traversal

A nested loop performs an operation for every pair of loop iterations.

Time Complexity:

- O(n²)

Space Complexity:

- O(1)

### Recursive Factorial

Recursive Factorial calculates n! using recursive function calls.

Time Complexity:

- O(n)

Space Complexity:

- O(n)

The additional space is required by the recursion call stack.

### Iterative Factorial

Iterative Factorial calculates n! using a loop and an accumulator.

Time Complexity:

- O(n)

Space Complexity:

- O(1)

---

# 3. Project Structure

```text
daa_lab2/
│
├── app.py
├── search_analysis.py
├── code_benchmark.py
├── benchmark_engine.py
├── complexity_analysis.py
├── visualization.py
├── requirements.txt
├── README.md
│
├── graphs/
│   ├── search_time.png
│   ├── factorial_time.png
│   ├── loop_time.png
│   └── memory_comparison.png
│
├── results/
│   └── benchmark_results.csv
│
├── report/
│
└── venv/

# 4. Technologies Used

The project was developed using Python.

Main libraries used:

- Streamlit
- NumPy
- Pandas
- Matplotlib
- memory_profiler
- Jupyter

Python virtual environment was used to isolate the project's dependencies.

---

# 5. Search Analysis Module

The `search_analysis.py` file implements:

- Linear Search
- Binary Search
- Comparison counting
- First-occurrence detection

The search algorithms return:

- Index of the target
- Number of comparisons

Binary Search continues searching toward the left after finding the target so that the first occurrence is returned when duplicate values exist.

---

# 6. Code Benchmarking Module

The `code_benchmark.py` file contains four programs:

1. Single Loop Traversal
2. Nested Loop Traversal
3. Recursive Factorial
4. Iterative Factorial

These programs demonstrate how different programming structures behave as input size increases.

---

# 7. Automated Benchmarking Engine

The `benchmark_engine.py` module provides a reusable benchmarking engine.

It measures:

- Algorithm name
- Input size
- Execution time
- Peak memory usage

Execution time is measured using Python's `time` module.

Memory usage is measured using Python's `tracemalloc`.

The collected results are converted into a Pandas DataFrame and saved as:

```text
results/benchmark_results.csv
```

---

# 8. Complexity Analysis Module

The `complexity_analysis.py` module contains the theoretical complexity comparison of the implemented algorithms.

The comparison includes:

| Algorithm / Program | Best Case | Average Case | Worst Case | Space |
| ------------------- | --------- | ------------ | ---------- | ----- |
| Linear Search       | O(1)      | O(n)         | O(n)       | O(1)  |
| Binary Search       | O(1)      | O(log n)     | O(log n)   | O(1)  |
| Single Loop         | O(n)      | O(n)         | O(n)       | O(1)  |
| Nested Loop         | O(n²)     | O(n²)        | O(n²)      | O(1)  |
| Recursive Factorial | O(n)      | O(n)         | O(n)       | O(n)  |
| Iterative Factorial | O(n)      | O(n)         | O(n)       | O(1)  |

---

# 9. Visualization Module

The `visualization.py` module generates performance graphs.

The generated graphs include:

### Search Algorithm Comparison

```text
graphs/search_time.png
```

This graph compares the execution time of Linear Search and Binary Search for different input sizes.

### Factorial Comparison

```text
graphs/factorial_time.png
```

This graph compares Recursive Factorial and Iterative Factorial.

### Loop Comparison

```text
graphs/loop_time.png
```

This graph compares Single Loop and Nested Loop performance.

### Memory Comparison

```text
graphs/memory_comparison.png
```

This graph compares the memory usage of the implemented algorithms and programs.

---

# 10. Experimental Results

The automated benchmarking engine produced experimental measurements for different input sizes.

The benchmark results are stored in:

```text
results/benchmark_results.csv
```

The measurements demonstrate how execution time and memory usage change as input size increases.

---

# 11. Observations

## Linear Search vs Binary Search

Linear Search may need to inspect many elements before finding a target or determining that the target is absent.

Binary Search repeatedly halves the search space and therefore scales much better for large sorted datasets.

The experiment demonstrates the practical difference between O(n) and O(log n) search behavior.

---

## Single Loop vs Nested Loop

The Single Loop performs one traversal of the input and therefore has O(n) time complexity.

The Nested Loop performs approximately n × n operations and therefore has O(n²) time complexity.

As input size increases, the execution time of the Nested Loop increases much more rapidly.

---

## Recursive Factorial vs Iterative Factorial

Both factorial implementations perform O(n) computational work.

However, Recursive Factorial uses the function call stack and therefore requires O(n) additional space.

Iterative Factorial uses a loop and constant auxiliary space.

The experimental results show that the iterative implementation generally requires less execution time and memory than the recursive implementation for the tested inputs.

---

# 12. Time-Space Trade-Off

The project demonstrates that algorithm selection involves both time and space considerations.

Binary Search provides faster search growth than Linear Search but requires the input data to be sorted.

Recursive Factorial has the same asymptotic time complexity as Iterative Factorial but requires additional stack memory.

Iterative Factorial avoids recursive call-stack growth and therefore provides O(1) auxiliary space.

---

# 13. Conclusion

The Algorithm Performance Measurement and Benchmarking Tool demonstrates how theoretical algorithmic complexity relates to actual experimental performance.

The experiments show that:

- Binary Search scales better than Linear Search for sorted datasets.
- Single Loop Traversal scales better than Nested Loop Traversal.
- Recursive Factorial uses additional stack memory.
- Iterative Factorial provides constant auxiliary space.
- Increasing input size makes differences between algorithmic complexities increasingly visible.
- Execution time and memory usage provide practical evidence for evaluating algorithm performance.

The project combines algorithm implementation, benchmarking, complexity analysis, data collection, and visualization into a single performance analysis workflow.

---

# 14. Future Enhancements

Possible future improvements include:

- Adding more searching and sorting algorithms.
- Supporting user-defined Python code snippets.
- Adding multiple benchmark runs and average execution time.
- Adding standard deviation and statistical analysis.
- Allowing users to export benchmark reports.
- Adding interactive graphs.
- Adding additional memory profiling techniques.
- Supporting larger datasets.
- Improving the Streamlit user interface.
- Adding automatic report generation.

---

# 15. How to Run the Project

## Step 1: Activate the Virtual Environment

### Windows

```text
venv\Scripts\activate
```

## Step 2: Install Dependencies

```text
pip install -r requirements.txt
```

## Step 3: Run the Streamlit Application

```text
streamlit run app.py
```

The application can then be opened in the browser using the Streamlit URL displayed in the terminal.

---

# 16. Individual Python Modules

The project contains separate modules for different responsibilities:

| File | Purpose |
| ---- | ------- |
| `app.py` | Streamlit web application |
| `search_analysis.py` | Linear and Binary Search implementation |
| `code_benchmark.py` | Loop and Factorial implementations |
| `benchmark_engine.py` | Automated performance measurement |
| `complexity_analysis.py` | Complexity comparison |
| `visualization.py` | Graph generation |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

# 17. Repository Contents

The GitHub repository contains the source code, benchmarking results, generated graphs, documentation, and report files required for the assignment.

This project was developed individually as part of the Design and Analysis of Algorithms Lab.

---

## Author

**Akash Sharma**

BCA (AI & DS)  
K.R. Mangalam University  
Roll Number: 2401201108