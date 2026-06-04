from tkinter import messagebox, filedialog

def abrir_archivo(text_widget):
    try:
        ruta_archivo = filedialog.askopenfilename(
            title="Abrir archivo",
            filetypes=[
                ("Archivos de texto", "*.txt"),
                ("Todos", "*.*")
            ],
        )

        if not ruta_archivo:
            return

        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

        text_widget.delete("1.0", "end")
        text_widget.insert("1.0", contenido)

    except Exception as error_archivo:
        messagebox.showerror("Error", f"Ha ocurrido un error: {error_archivo}")