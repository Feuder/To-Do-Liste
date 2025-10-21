import tkinter as tk
from tkinter import ttk
import json
import os
import uuid
from datetime import datetime, timezone

add_Window = tk.Tk()
add_Window.title("TO DOs")
add_Window.geometry("520x450")
add_Window.configure(bg="gray20")

ToDos = []

def main():
    ToDos = ToDo.Todos_laden()
    Startseite(ToDos)

def Startseite(ToDos):
   
    style = ttk.Style()
    style.configure("Todo.TLabelframe", background="#E0E0E0")
    style.configure("Todo.TLabelframe.Label", background="#E0E0E0") 
    style.configure("Todo.TCheckbutton",
                    background="#E0E0E0",
                    foreground="black",
                    focuscolor="#E0E0E0")

    Todos_rahmen = ttk.LabelFrame(add_Window, text="Zu erledigende ToDos", style="Todo.TLabelframe", padding=(10, 10))
    Todos_rahmen.grid(row=0, column=0, sticky="w", padx=10, pady=10)
    Todos_rahmen.config(width=240, height=360)
    Todos_rahmen.grid_propagate(False)

    Erl_Todos_rahmen = ttk.LabelFrame(add_Window, text=("Erledigte ToDos"),style="Todo.TLabelframe", padding=(10,10))
    Erl_Todos_rahmen.grid(row=0, column=1, sticky="s", padx=10, pady=10)
    Erl_Todos_rahmen.config(width=240, height=360)
    Erl_Todos_rahmen.grid_propagate(False)

    Todos_laden(Todos_rahmen, ToDos)

    neue_ToDos_btn = ttk.Button(
        add_Window,
        text=("Neue Frage hinzufügen"),
        command=lambda: todo_hinzufuegen(Todos_rahmen)
    )
    neue_ToDos_btn.grid(row=3, column=0, padx=10, pady=10)

    add_Window.mainloop()

def Todos_laden(Todos_rahmen, ToDos):

    row_zu_erl = 1
    row_erl = 1

    for i in ToDos:
        if i.done:
            zu_erld_todos_checkbutton = ttk.Checkbutton(Todos_rahmen, text=i.text, style="Todo.TCheckbutton")
            zu_erld_todos_checkbutton.grid(row=row_zu_erl, column=0, sticky="w", padx=10, pady=2)
            row_erl += 1
        else:
            zu_erld_todos_checkbutton = ttk.Checkbutton(Todos_rahmen, text=i.text, style="Todo.TCheckbutton")
            zu_erld_todos_checkbutton.grid(row=row_zu_erl, column=0, sticky="w", padx=10, pady=2)
            row_zu_erl += 1



def todo_hinzufuegen(Todos_rahmen):
    neue_Todo = tk.Toplevel(add_Window)
    neue_Todo.title("Neue ToDo erstellen")
    neue_Todo.geometry("250x150")
    neue_Todo.configure(bg="gray25")

    neue_Aufgabe_label = ttk.Label(neue_Todo, text="Hier neue ToDo eintragen:", background="gray25", justify="center")
    neue_Aufgabe_label.grid(row=0, column=0, padx=10, pady=10)

    neue_Aufgabe = ttk.Entry(neue_Todo, width=35)
    neue_Aufgabe.grid(row=1, column=0,padx=10, pady=10, sticky="ew")
    neue_Todo.columnconfigure(0, weight=1)

    absenden_btn = ttk.Button(
        neue_Todo, text="Fertig",
        command=lambda: Todo_absenden()
        )
    absenden_btn.grid(row=2, column=0, padx=10, pady=10)


    def Todo_absenden():
        text = neue_Aufgabe.get().strip()
        if not text:
            return
        todo = ToDo.TODO_ers(text=text)
        ToDos.append(todo)
        todo.Todos_speichern()
        Todos_laden(Todos_rahmen)
        neue_Todo.destroy()


class ToDo:

    def __init__(self, id, text, erstellt_am, done, erledigt_am):
        self.id = id
        self.text = text
        self.erstellt_am = erstellt_am
        self.done = done
        self.erledigt_am = erledigt_am


    @classmethod
    def TODO_ers(cls, text: str) -> "ToDo":
        return cls(
            id=str(uuid.uuid4()),
            text=text,
            done = False,
            erstellt_am=datetime.now(timezone.utc).isoformat(),
            erledigt_am = ""
        )
            
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "text": self.text,
            "erstellt_am": self.erstellt_am,
            "done": self.done,
            "erledigt_am": self.erledigt_am,
        }
    
    def Todos_speichern(self, pfad="todo.json"):
        try:
            with open(pfad, "r", encoding="utf-8") as f:
                try:
                    daten = json.load(f)
                except json.JSONDecodeError:
                    daten = []
        except FileNotFoundError:
            daten = []

        daten.append(self.to_dict())

        try:
            with open(pfad, "w", encoding="utf-8") as f:
                json.dump(daten, f, ensure_ascii=False, indent=2)
        except Exception as e:             
            return

    def Todos_laden(pfad="todo.json"):
        try:
            with open(pfad, "r", encoding="utf-8") as f:
                daten = json.load(f)
            return [ToDo(**todo) for todo in daten]
        except FileNotFoundError:
            return[]
main()