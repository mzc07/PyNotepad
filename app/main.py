import tkinter as tk
from editor import Editor
from menubar import MenuBar

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('PyNotepad')
        self.minsize(400,300)
        self.resizable(True,True)
        self.menubar = MenuBar(self)
        self.editor = Editor(self)
        


    def run(self):
        self.mainloop()





if __name__ == '__main__':
    app = Aplicacion()
    app.run()