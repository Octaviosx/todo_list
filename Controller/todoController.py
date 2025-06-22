class TodoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        self.view.buttonAdd.configure(command=self.add_task)
        self.view.buttonDelete.configure(command=self.delete_task)
        
    def add_task(self):
        task = self.view.get_task_ingressed()
        self.model.add_task(task)
        self.view.clean_entry()
        self.update_view()
        
    def delete_task(self):
        index = self.view.get_index_seleccted()
        if index is not None:
            self.model.delete_task(index)
            self.update_view()
    
    def update_view(self):
        tasks = self.model.get_tasks()
        self.view.update_list(tasks)