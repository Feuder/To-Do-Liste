import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Checkliste")
root.geometry("250x200")

# Beispiel-Einträge
eintraege = ["Aufgabe 1", "Aufgabe 2", "Aufgabe 3"]

# Variablen speichern den Zustand (0 = aus, 1 = an)
variablen = []

for text in eintraege:
    chk = ttk.Checkbutton(root, text=text, offvalue=1)
    chk.pack(anchor="w", padx=10, pady=2)

root.mainloop()
