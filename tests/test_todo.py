from lib.todo import *
from lib.todo_list import *
import pytest

'''
Given a task
#task property should be set to task
'''
def test_todo_task_is_set():
    task1 = Todo("Do anything")
    assert task1.task == "Do anything"

'''
Given a task
#complete property should be set to False
'''
def test_todo_complete_is_set_to_false():
    task1 = Todo("Do anything")
    assert task1.complete == False
    
