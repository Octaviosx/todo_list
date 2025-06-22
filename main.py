from Controller.todoController import *
from Model.model import *
from View.viewTask import *
import tkinter as tk
import customtkinter as ctk

if __name__ == "__main__":
    #window = tk.Tk()
    window = ctk.CTk()
    model = TodoModel()
    view = TodoView(window)
    controller = TodoController(model, view)
    controller.update_view()
    window.mainloop()