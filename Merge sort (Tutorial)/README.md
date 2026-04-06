# Merge Sort Implementation in Python

A clean, recursive implementation of the **Merge Sort** algorithm. This project demonstrates the "Divide and Conquer" paradigm, a fundamental concept in computer science and technical interviews.

---

## What is Merge Sort?

Merge Sort is an $O(n \log n)$ comparison-based sorting algorithm. It works by recursively breaking down a list into several sub-lists until each sub-list consists of a single element, and then merging those sub-lists in a manner that results in a sorted list.

### The "Divide and Conquer" Strategy
1.  **Divide:** Split the unsorted list into two halves.
2.  **Conquer:** Recursively call `mergeSort` on both halves.
3.  **Combine:** Use the `merge` function to put the pieces back together in the correct order.

---

## Visual Walkthrough

Given the input: `[3, 1, 2, 10, -3]`

### 1. The Recursive Split (Depth-First)
The algorithm dives deep into the **left** side before ever touching the right side:
* `[3, 1, 2, 10, -3]` → Left: `[3, 1]`
* `[3, 1]` → Left: `[3]`, Right: `[1]`
* **Base Case reached!** `[3]` and `[1]` are returned to be merged.

### 2. The Merge Step
Once the halves are returned, they are compared one-by-one:
* `merge([3], [1])` → **`[1, 3]`**
* `merge([10], [-3])` → **`[-3, 10]`**
* `merge([2], [-3, 10])` → **`[-3, 2, 10]`**
* **Final Merge:** `merge([1, 3], [-3, 2, 10])` → **`[-3, 1, 2, 3, 10]`**

---

## Performance Summary

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Best Time** | $O(n \log n)$ | Consistent performance regardless of input order. |
| **Average Time** | $O(n \log n)$ | Standard performance for most cases. |
| **Worst Time** | $O(n \log n)$ | Even with reverse-sorted data, it maintains speed. |
| **Space** | $O(n)$ | Requires extra memory for the temporary merged lists. |
| **Stability** | **Stable** | Preserves the relative order of equal elements. |

---

## 💻 How to Use

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Confy-Code/My_HacherRank_solutions.git]

or just copy-paste and run the python script in your favorite IDE.