import tkinter as tk
from tkinter import ttk

add_Window = tk.Tk()
add_Window.title("TO DOs")
add_Window.geometry("520x500")
add_Window.configure(bg="gray20")

Fragen = []
Erl_Frage = []


def main():
    style = ttk.Style()
    style.configure("Todo.TLabelframe", background="#E0E0E0")
    style.configure("Todo.TLabelframe.Label", background="#E0E0E0") 

    Todos_rahmen = ttk.LabelFrame(add_Window, text="Zu erledigende ToDos", style="Todo.TLabelframe", padding=(10, 10))
    Todos_rahmen.grid(row=0, column=0, sticky="w", padx=10, pady=10)
    Todos_rahmen.config(width=240, height=360)
    Todos_rahmen.grid_propagate(False)

    Erl_Todos_rahmen = ttk.LabelFrame(add_Window, text=("Erledigte ToDos"),style="Todo.TLabelframe", padding=(10,10))
    Erl_Todos_rahmen.grid(row=0, column=1, sticky="s", padx=10, pady=10)
    Erl_Todos_rahmen.config(width=240, height=360)
    Erl_Todos_rahmen.grid_propagate(False)

    zu_erld_todos_label = ttk.Label(
        Todos_rahmen,
        wraplength=250, justify="left"
    )
    zu_erld_todos_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    erl_todos_label = ttk.Label(
        Erl_Todos_rahmen,
        wraplength=250, justify="right"
    )
    erl_todos_label.grid(row=0, column=0, sticky="s", padx=10, pady=10)

    neue_ToDos_btn = ttk.Button(
        text=("Neue Frage hinzufügen"),
        command=lambda: todo_hinzufuegen()
    )
    neue_ToDos_btn.grid(row=3, column=0, padx=10, pady=10)

    add_Window.mainloop()

def todo_hinzufuegen():
    neue_Todo = tk.Toplevel(add_Window)
    neue_Todo.title("Neue ToDo erstellen")
    neue_Todo.geometry("250x150")
    neue_Todo.configure(bg="gray25")

    neue_frage_label = ttk.Label(neue_Todo, text="Hier neue ToDo eintragen:", background="gray25", justify="center")
    neue_frage_label.grid(row=0, column=0, padx=10, pady=10)

    neue_frage = ttk.Entry(neue_Todo, width=35)
    neue_frage.grid(row=1, column=0,padx=10, pady=10, sticky="ew")

    absenden_btn = ttk.Button(
        neue_Todo, text="Fertig",
        command=lambda: Todo_Speichern()
        )
    absenden_btn.grid(row=2, column=0, padx=10, pady=10)

    def Todo_Speichern():
        Todo =neue_frage.get().strip()

        if Todo:
            Fragen.append(Todo)
        neue_Todo.destroy()

        for i in Fragen:
            print(i)



main()