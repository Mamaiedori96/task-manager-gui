# 📝 Task Manager GUI

A modern and beginner-friendly **Task Manager desktop application** built with Python and Tkinter.

This project allows users to organize their daily tasks, track their progress, and automatically save their data using JSON.

## ✨ Features

- ➕ **Add Tasks** – Create new tasks quickly and easily.
- 🗑️ **Delete Tasks** – Remove tasks you no longer need.
- ✏️ **Edit Tasks** – Modify existing tasks.
- 🔍 **Search Tasks** – Find tasks using keywords.
- ✅ **Complete Tasks** – Mark tasks as completed.
- ↩️ **Undo Completion** – Restore completed tasks to their unfinished state.
- 📊 **Progress Tracking** – View your completion percentage with a progress bar.
- 💾 **Automatic Saving** – Save tasks locally using JSON.
- 🌙 **Dark Theme** – A clean, dark-themed graphical interface.

## 🛠️ Technologies Used

- **Python** – Main programming language
- **Tkinter** – Graphical user interface
- **JSON** – Local data storage
- **ttk** – Progress bar widget

## 🚀 Getting Started

### Requirements

- Python 3.9 or newer
- Tkinter (usually included with Python)

### Installation

1. Download or clone this repository.
2. Open the project folder.
3. Run the application:

```bash
python main.py
```

The Task Manager window will open automatically.

## 📁 Project Structure

```text
task_manager_gui/
├── main.py
├── tasks.json
└── README.md
```

## 📊 How Progress Tracking Works

The application calculates the percentage of completed tasks:

**Progress = (Completed Tasks / Total Tasks) × 100**

For example, completing 2 out of 4 tasks results in **50% progress**.

The progress bar updates automatically when tasks are added, deleted, completed, or marked as unfinished.

## 💡 What I Learned

While building this project, I practiced:

- Creating graphical interfaces with Tkinter
- Working with Python functions and callbacks
- Handling user input and events
- Managing lists and task selections
- Reading and writing JSON files
- Using conditions and string methods
- Updating interface elements dynamically
- Organizing a Python project

## 🔮 Future Improvements

- Task deadlines
- Task priority levels
- Task categories
- Improved interface styling
- Sorting and filtering tasks

## 📌 About This Project

This project was created as part of my Python learning journey to improve my programming skills through practical applications.

It represents my progress in building functional desktop applications and understanding how different Python concepts work together.

---

**Built with Python 🐍 | Learning by Building 🚀**