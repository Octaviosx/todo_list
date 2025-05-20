import tkinter as tk
import tkinter.font as tkFont

class TodoView:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1280x720")
        self.window.title("To-do List Octaviosx")
        self.window.iconbitmap("src/icons/todo_list.ico")
        self.window.configure(bg='gray98')
        fuente_global = tkFont.Font(family="Roboto")
        self.window.option_add("*Font", fuente_global)
        
        self.entry = tk.Entry(window, width=40, bg="azure")
        self.entry.pack(pady=10)
        
        self.buttonAdd = tk.Button(window, text='Agregar tarea', bg="DodgerBlue2", fg="white")
        self.buttonAdd.pack()
        
        self.list = tk.Listbox(window, width=50, height=10, bg="gray98")
        self.list.pack(pady=10)
        
        self.buttonDelete = tk.Button(window, text="Eliminar tarea seleccionada",  bg="DodgerBlue2", fg="white")
        self.buttonDelete.pack(pady=5)
        
    def get_task_ingressed(self):
        return self.entry.get()
    
    def clean_entry(self):
        self.entry.delete(0, tk.END)
        
    def update_list(self, tasks):
        self.list.delete(0, tk.END)
        for task in tasks:
            self.list.insert(tk.END, task)
            
    def get_index_seleccted(self):
        selecction = self.list.curselection()
        return selecction[0] if selecction else None