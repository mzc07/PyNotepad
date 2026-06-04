import tkinter as tk
from file_handler import seleccionar_archivo

class MenuBar:
    def __init__(self, parent):
        super().__init__()
        self.menubar = tk.Menu(parent)

        self.menuarchivo = tk.Menu(self.menubar, tearoff=False)

        self.menuarchivo.add_command(label="Abrir", command=seleccionar_archivo, accelerator="Ctrl+O")
        self.menuarchivo.add_command(label="Nuevo")
        self.menuarchivo.add_command(label="Salir", command=parent.destroy)
        
        self.menubar.add_cascade(menu=self.menuarchivo, label="Archivo")

        self.menuver = tk.Menu(self.menubar, tearoff=False)
        self.menuver.add_command(label="Zoom in")

        self.menubar.add_cascade(menu=self.menuver, label="Ver")
        parent.config(menu=self.menubar)
