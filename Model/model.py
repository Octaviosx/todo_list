class TodoModel:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, tarea):
        if tarea:
            self.tasks.append(tarea)
            
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
    
    def get_tasks(self):
        return self.tasks