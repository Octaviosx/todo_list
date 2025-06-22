import tkinter as tk
import tkinter.font as tkFont
import customtkinter as ctk
from PIL import Image

class TodoView:
    def __init__(self, window):
        ctk.set_appearance_mode("dark")  
        ctk.set_default_color_theme("blue")
        self.window = window
        self.window.geometry("650x650")
        self.window.title("To-do List Octaviosx")
        self.window.iconbitmap("src/icons/todo_list.ico")
        self.window.configure(fg_color=ctk.ThemeManager.theme["CTk"]["fg_color"])
        fuente_global = tkFont.Font(family="Roboto")
        self.window.option_add("*Font", fuente_global)
        
        image = Image.open("D:/universidad/to-do-list/todo_list/src/icons/hybridge_log.png")
        image = image.resize((400, 400))  # Ajusta tamaño aquí
        self.ctk_image = ctk.CTkImage(light_image=image, dark_image=image)
        self.label_img = ctk.CTkLabel(window, image=self.ctk_image, text="")
        self.label_img.pack(pady=10)
        
        self.entry = ctk.CTkEntry(window, width=200, fg_color="azure", text_color='black')
        self.entry.pack(pady=10)
        
        self.buttonAdd = ctk.CTkButton(window, text='Agregar tarea', corner_radius=15, fg_color="DodgerBlue2", text_color="white")
        self.buttonAdd.pack()
        
        self.list = tk.Listbox(window, width=50, height=10, bg="gray98")
        self.list.pack(pady=10)
        
        self.buttonDelete = ctk.CTkButton(window, text="Eliminar tarea seleccionada", corner_radius=15, fg_color="DodgerBlue2", text_color="white")
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