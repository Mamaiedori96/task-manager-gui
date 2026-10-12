
import tkinter as tk
import json
from tkinter import messagebox, simpledialog, ttk

window = tk.Tk()
window.title("Task Manager")
window.geometry("600x750")
window.configure(bg="#1e1e2e")


def adauga_task(event=None):
    task = camp_task.get().strip()

    if not task:
        messagebox.showwarning("Task gol!", "Introdu un task!")
        return

    taskuri_existente = lista_taskuri.get(0, tk.END)

    if task in taskuri_existente:
        messagebox.showwarning("Task duplicat", "Acest task exista deja!")
        return

    lista_taskuri.insert(tk.END, task)
    camp_task.delete(0, tk.END)
    salveaza_taskuri()
    actualizeaza_progres()


def sterge_task():
    selectie = lista_taskuri.curselection()

    if not selectie:
        messagebox.showwarning("Eroare", "Selecteaza un task!")
        return

    lista_taskuri.delete(selectie[0])
    salveaza_taskuri()
    actualizeaza_progres()


def finalizeaza_task():
    selectie = lista_taskuri.curselection()

    if not selectie:
        messagebox.showwarning("Eroare", "Selecteaza un task!")
        return

    index = selectie[0]
    task = lista_taskuri.get(index)

    if not task.endswith(" - Finalizat"):
        lista_taskuri.delete(index)
        lista_taskuri.insert(index, task + " - Finalizat")
        lista_taskuri.selection_set(index)
        salveaza_taskuri()
        actualizeaza_progres()


def anuleaza_finalizare():
    selectie = lista_taskuri.curselection()
    
    if not selectie:
        messagebox.showwarning("Eroare", "Selecteaza un task!")
        return
    
    index = selectie = [0]
    task = lista_taskuri.get(index)
    
    if task.endswith(" - Finalizat"):
        task_nou = task.removesuffix(" - Finalizat")
        lista_taskuri.delete(index)
        lista_taskuri.insert(index, task_nou)
        salveaza_taskuri()
        actualizeaza_progres()
        
    

def editeaza_task():
    selectie = lista_taskuri.curselection()

    if not selectie:
        messagebox.showwarning("Eroare", "Selecteaza un task!")
        return

    index = selectie[0]
    task = lista_taskuri.get(index)

    nume_nou = simpledialog.askstring(
        "Edit Task",
        "Introdu noul nume:",
        initialvalue=task,
        parent=window
    )

    if nume_nou is None:
        return

    nume_nou = nume_nou.strip()

    if not nume_nou:
        messagebox.showwarning("Eroare", "Numele nu poate fi gol!")
        return

    taskuri_existente = lista_taskuri.get(0, tk.END)

    if any(
        nume_nou == existent
        for i, existent in enumerate(taskuri_existente)
        if i != index
    ):
        messagebox.showwarning("Eroare", "Acest task exista deja!")
        return

    lista_taskuri.delete(index)
    lista_taskuri.insert(index, nume_nou)
    lista_taskuri.selection_set(index)

    salveaza_taskuri()
    actualizeaza_progres()

def cauta_task():
    cautare = camp_cautare.get().strip().lower()

    if not cautare:
        return

    taskuri = lista_taskuri.get(0, tk.END)

    for index, task in enumerate(taskuri):
        if cautare in task.lower():
            lista_taskuri.selection_clear(0, tk.END)
            lista_taskuri.selection_set(index)
            lista_taskuri.see(index)
            lista_taskuri.activate(index)
            return

    messagebox.showinfo("Search Task", "Nu am gasit task-ul!")

def salveaza_taskuri():
    tasks = list(lista_taskuri.get(0, tk.END))

    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def incarca_taskuri():
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            tasks = json.load(f)

        for task in tasks:
            lista_taskuri.insert(tk.END, task)

    except FileNotFoundError:
        pass

    except (json.JSONDecodeError, OSError):
        messagebox.showwarning(
            "Eroare",
            "Nu am putut incarca fisierul tasks.json!"
        )

def actualizeaza_progres():
    taskuri = lista_taskuri.get(0, tk.END)

    total = len(taskuri)

    finalizate = sum(
        1 for task in taskuri
        if task.endswith(" - Finalizat")
    )

    if total > 0:
        procent = (finalizate / total) * 100
    else:
        procent = 0

    label_progres.config(
        text=f"Completed: {finalizate}/{total} ({procent:.0f}%)"
    )

    bara_progres["value"] = procent


titlu = tk.Label(
    window,
    text="Welcome to Task Manager!",
    font=("Arial", 20),
    fg="white",
    bg="#1e1e2e"
)
titlu.pack(pady=10)


camp_task = tk.Entry(
    window,
    width=45,
    font=("Arial", 12)
)
camp_task.pack(pady=5)
camp_task.bind("<Return>", adauga_task)


buton = tk.Button(
    window,
    text="Add Task",
    bg="green",
    fg="white",
    padx=15,
    pady=8,
    command=adauga_task
)
buton.pack(pady=5)


lista_taskuri = tk.Listbox(
    window,
    width=45,
    height=10,
    bg="#313244",
    fg="white",
    selectbackground="#585b70",
    font=("Arial", 11)
)
lista_taskuri.pack(pady=10)


buton_stergere = tk.Button(
    window,
    text="Delete Task",
    bg="red",
    fg="white",
    padx=15,
    pady=8,
    command=sterge_task
)
buton_stergere.pack(pady=5)


buton_finalizare = tk.Button(
    window,
    text="Complete Task",
    bg="green",
    fg="white",
    padx=15,
    pady=8,
    command=finalizeaza_task
)
buton_finalizare.pack(pady=5)

buton_anulare = tk.Button(
    window,
    text="Undo Complete",
    command=anuleaza_finalizare
)
buton_anulare.pack(pady=5)

buton_editare = tk.Button(
    window,
    text="Edit Task",
    bg="#89b4fa",
    fg="black",
    padx=15,
    pady=8,
    command=editeaza_task
)
buton_editare.pack(pady=5)


camp_cautare = tk.Entry(
    window,
    width=35,
    font=("Arial", 11)
)
camp_cautare.pack(pady=5)


buton_cautare = tk.Button(
    window,
    text="Search Task",
    bg="#cba6f7",
    fg="black",
    padx=15,
    pady=8,
    command=cauta_task
)
buton_cautare.pack(pady=5)


label_progres = tk.Label(
    window,
    text="Completed: 0/0 (0%)",
    font=("Arial", 12),
    fg="white",
    bg="#1e1e2e"
)
label_progres.pack(pady=10)

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Custom.Horizontal.TProgressbar",
    troughcolor="#45475a",
    background="#a6e3a1",
    bordercolor="#45475a",
    lightcolor="#a6e3a1",
    darkcolor="#a6e3a1",
    thickness=20
)


bara_progres = ttk.Progressbar(
    window,
    length=300,
    maximum=100,
    mode="determinate",
    style="Custom.Horizontal.TProgressbar"
)
bara_progres.pack(pady=10)

incarca_taskuri()
actualizeaza_progres()

window.mainloop()