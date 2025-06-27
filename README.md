# 🧠 Task Manager Simulator 

A simple Python command-line task manager that uses a queue-based system to manage tasks by priority, duration, and title. 
The project demonstrates custom queue handling, binary search, and sorting — great for learning data structures and control flow.

---

## 📌 Features

- Add and store tasks with a **title**, **duration** (in minutes), and **priority** (lower number = higher priority).
- Complete the **next most urgent task** based on priority.
- **Search** for tasks using **binary search** (after sorting alphabetically).
- **Sort** tasks by **duration** (ascending).
- Simple, user-friendly CLI menu with input validation and error handling.

---

## 🛠️ Functions Implemented

### 🔁 Queue Functions
- `insert(queue, task)`
- `extract(queue)`
- `peek(queue)`
- `is_empty(queue)`

### ⚙️ Task Functions
- `complete_next_task(queue)`
- `search_for_task(queue, title)` *(uses binary search)*
- `sort_tasks(queue)` *(by duration ascending)*

---

## 🚀 How to Run

1. **Clone the repo** or copy the code into a `.py` file:
   ```bash
   git clone https://github.com/yourusername/task-manager-python.git
   cd task-manager-python

   
2. Run the script using Python:
```bash
python task_manager.py



