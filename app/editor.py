import tkinter as tk

class Editor():
    def __init__(self, parent):
        self.scrollbar = tk.Scrollbar(parent)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text = tk.Text(parent, font=("Courier",12), bg='#ffffff' ,yscrollcommand=self.scrollbar.set)
        self.text.pack(side=tk.LEFT,expand=True, fill="both")