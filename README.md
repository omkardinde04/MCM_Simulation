AOA_IA
# 🔗 Matrix Chain Multiplication Simulator

A **web-based visual simulator** for the Matrix Chain Multiplication (MCM) problem using **Flask**, **HTML**, **CSS**, and **JavaScript**. Built as part of our **AOA (Analysis of Algorithms) Internal Assessment**.

---

## 🚀 Features

- 📥 Accepts any list of matrix dimensions as input
- 🧠 Backend computes the optimal multiplication order using **Dynamic Programming**
- 🧮 Visualizes the DP matrix table updates in real-time
- 📜 Shows each step's expression and result
- ✨ Highlights updated cells in the matrix
- 🎨 Dark-mode themed clean user interface

--- 

## 🧠 How It Works

1. **User Input**: User enters dimensions (e.g., `90,234,4,3,52,52`).
2. **Backend (`app.py`)**:
   - Runs Matrix Chain Multiplication using dynamic programming.
   - Tracks the cost and steps for every sub-problem.
3. **Frontend (`index.html` + JS)**:
   - Creates a visual matrix (DP table).
   - Shows each calculation step with animation.
   - Highlights updated matrix cells.
   - Displays computation expressions like:
     ```
     0 + 0 + 90*234*4 = 84240
     ```

The process continues step-by-step, visualizing updates in the matrix and showing how the optimal order is found.

---

## 🧑‍💻 Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Styling**: Pure CSS with smooth transitions
- **Visualization**: Dynamic DP table using JS

---



