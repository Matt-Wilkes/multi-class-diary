from lib.todo import *
class TodoList:
    def __init__(self):
        self.todos = []
        
    def add(self,todo):
        self.todo = todo
        if self.todo.task == '':
           raise Exception("Task is empty")
        elif type(self.todo.task) != str:
            raise Exception("Only strings can be added")
        self.todos.append(todo)
    def incomplete(self):
        incomplete_tasks = list(filter(lambda task: task.complete == False, self.todos))
        return incomplete_tasks
    def complete(self):
        complete_tasks = list(filter(lambda task: task.complete == True, self.todos))
        return complete_tasks

            