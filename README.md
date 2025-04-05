# Programming Assignment 1

## Overview
This assignment focuses on numerical methods covered in Chapters 5 and 6, including:

- **Gaussian Elimination with Backward Substitution**  
- **LU Factorization**  
- **Diagonal Dominance Check**  
- **Positive Definiteness Test**

These methods help solve systems of equations and analyze matrix properties using various algorithmic techniques.

---

## Project Structure
```
cot-4500-as3b/
├── src/
│   ├── main/
│   │   ├── __init__.py
│   │   └── assignment_3.py
│   └── test/
│       ├── __init__.py
│       └── test_assignment_3.py
├── requirements.txt
└── README.md
```

- **assignment_3.py**: Contains the implementation of all four problems (P1 to P4).
- **test_assignment_3.py**: Includes test cases and prints results formatted to match expected output.
- **requirements.txt**: Lists required libraries (only NumPy if used).
- **README.md**: Provides setup steps, run instructions, and file structure overview.

---

## Requirements
- **Python 3.x** (Recommended: 3.8+)
- No external libraries are required (uses Python's standard library).

If dependencies are added:
```bash
pip install -r requirements.txt
```

---

## How to Run

### 1. **Running the Algorithms Directly**
You can import and call functions (e.g., `P1`, `P2`, `P3`, `P4`) from `assignment_3.py` in your own Python scripts for manual testing.

### 2. **Running Test Cases**
To verify all outputs for the four problems with expected formatting, run the test script using:

```bash
python src/test/test_assignment_3.py
```

This will output:

- **P1 output**: Solution to the linear system using Gaussian elimination.
- **P2 output**: 2a. Matrix determinant, 2b. Lower triangular matrix L, 2c. Upper triangular matrix U
- **P3 output**: Lists required libraries (only NumPy if used).
- **P4 output**: Provides setup steps, run instructions, and file structure overview.
---
## Author
Jeffrey Chang 
Course: COT-4500 - Numerical Calculus  
Assignment: Programming Assignment 3b

