from tkinter import messagebox, filedialog

def seleccionar_archivo() -> None:
    try:
        ruta_archivo = filedialog.askopenfilename(
        title="Abrir archivo",
        filetypes=[("Archivos de texto","*.txt"),("Todos","*.")]
    )
    except Exception as error_archivo:
        messagebox.showerror('Error',f'Ha ocurrido un error: {error_archivo}')

