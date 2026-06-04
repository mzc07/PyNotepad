from file_handler import abrir_archivo
import tkinter as tk

class MenuBar:
    def __init__(self, parent, editor):
        self.menubar = tk.Menu(parent)

        self.menuarchivo = tk.Menu(self.menubar, tearoff=False)

        self.menuarchivo.add_command(
            label="Abrir",
            command=lambda: abrir_archivo(editor.text),
            accelerator="Ctrl+O"
        )

        self.menubar.add_cascade(menu=self.menuarchivo, label="Archivo")

        parent.config(menu=self.menubar)

        parent.bind(
            "<Control-o>",
            lambda event: abrir_archivo(editor.text)
        )