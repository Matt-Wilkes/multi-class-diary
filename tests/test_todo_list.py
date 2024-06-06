from lib.todo_list import *
'''
Initially TodoList contains no tasks
'''
def test_todo_list_initially_empty():
    todo_list = TodoList()
    assert todo_list.todos == []