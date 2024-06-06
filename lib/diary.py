from lib.diaryentry import DiaryEntry
from lib.todo_list import *
import re
import math

class Diary:
    def __init__(self):
        self.entries = []
    
    def add(self, entry):
        self.entries.append(entry)
    
    def all(self):
        if len(self.entries) > 0:
            return self.entries
        return "The diary is empty"

    
    def find_best_entry_for_reading_time(self, wpm, minutes):
        self.wpm = wpm
        self.minutes = minutes
        self.available = wpm * minutes
        if self.wpm <= 0 or self.minutes <= 0:
            raise Exception("Zero cannot be entered")
        while self.available > 0:
            for entry in self.entries:
                if len(entry.contents.split()) == self.available:
                    return entry
                else: 
                    self.available -= 1
        raise Exception("No diary entries can be read in given time")
    
    
    def get_contacts(self):
        pattern = "0\d{10}"
        contact_list = []
        for entry in self.entries:
            number = re.search(pattern, entry.contents)
            if number != None:
                contact_list.append(number.group())
                
        return contact_list
    
    def get_todo_list(self, todo_list):
        return TodoList.incomplete(todo_list)
    
    def complete_todo_list_item(self, task):
        Todo.mark_complete(task)