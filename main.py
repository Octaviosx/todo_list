import tkinter as tk
import tkinter.font as tkFont

ventana = tk.Tk()

ventana.title("To-do list Hybridge")
ventana.geometry("1280x720")
ventana.iconbitmap("src/icons/todo_list.ico")
ventana.configure(bg='white smoke')
#Agregar opacidad a la pagina
#ventana.attributes("-alpha", 0.9)

# Definir fuente global
fuente_global = tkFont.Font(family="Roboto")
ventana.option_add("*Font", fuente_global)

#encabezado
headSpace = tk.Frame(ventana)
headSpace.configure(width=1270, height=70, bg='white smoke', bd=5)

#Titulo To-do List
headSpace.pack()
tituloTodo_list = tk.Label(headSpace, text="To-do List Hybridge")
tituloTodo_list.config(bg='white smoke', font=("Roboto", 18, "bold"))
tituloTodo_list.place(rely=0.01)

#Boton crear tarea
btnCrear_tarea = tk.Button(headSpace, text='Agregar tarea')
btnCrear_tarea.config(fg="white", bg='DeepSkyBlue2', font=("Roboto", 00))

btnCrear_tarea.place(relx=0.90, rely=0.20)

#workspace
todoSpace = tk.Frame(ventana)
todoSpace.configure(width=1270, height=600, bg='white smoke', bd=5)

todoSpace.pack()

#Secciones por columna
todoSpace.grid_columnconfigure(1, minsize=415)
todoSpace.grid_columnconfigure(2, minsize=415)
todoSpace.grid_columnconfigure(3, minsize=415)
#Columna de tareas agregadas
taskList = tk.Label(todoSpace, text="Tareas por hacer", bg='white smoke')
taskList.grid(row=0, column=1, sticky='w')
#Columna de tareas en proceso
taskProceso = tk.Label(todoSpace, text="En proceso", bg='white smoke')
taskProceso.grid(row=0, column=2, sticky='w')
#Columna de tareas finalizadas
taskCompletada = tk.Label(todoSpace, text="Completadas", bg='white smoke')
taskCompletada.grid(row=0, column=3, sticky='w')


ventana.mainloop()