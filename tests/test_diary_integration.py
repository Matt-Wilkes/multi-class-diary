
from lib.diary import *
from lib.diaryentry import *
from lib.todo_list import *
from lib.todo import *
import pytest

'''
Given a diary entry is created
entries_list should be populated with the entry
'''
def test_diary_entry_updates_entries_list():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry","This is my first entry")
    diary.add(diary_entry1)
    assert diary.entries == [diary_entry1]
    
'''
Given there are diary entries
return a list of entries
'''

def test_all_returns_diary_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry","This is my first entry")
    diary.add(diary_entry1)
    assert diary.all() == [diary_entry1]

'''
Given there are no diary entries
Return a string "The diary is empty"
'''
def test_empty_diary_returns_error():
    diary = Diary()
    assert diary.all() == "The diary is empty"

'''
Given there are multiple diary entries
a list of the entries should be returned
'''

def test_all_returns_multiple_diary_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry","This is my first entry")
    diary_entry2 = DiaryEntry("second entry","This is my second entry")
    diary_entry3 = DiaryEntry("third entry","This is my third entry")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    assert diary.all() == [diary_entry1, diary_entry2, diary_entry3]

    
'''
Given wpm of 5 and 2 minutes
And an entry with a word length of 10
find_best_entry_for_reading_time should return the entry with 10 words
'''

def test_find_best_entry_for_reading_time_10_words():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry","This is my first entry, one two three four five")
    diary.add(diary_entry1)
    assert diary.find_best_entry_for_reading_time(5, 2) == diary_entry1
    
'''
Given entries contains three entries
8 words, 9 words and 11 words
And 5 wpm with 2 minutes is passed
find_best_entry_for_reading_time should return the entry with 9 words
'''
def test_find_best_entry_for_reading_time_three_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry", "one two three four five six seven eight")
    diary_entry2 = DiaryEntry("second entry", "one two three four five six seven eight nine")
    diary_entry3 = DiaryEntry("third entry", "one two three four five six seven eight nine ten eleven")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    assert diary.find_best_entry_for_reading_time(5, 2) == diary_entry2
    
'''
Given entries contains three entries
3 words, 6 words and 15 words
And 5 wpm with 2 minutes is passed
find_best_entry_for_reading_time should return the entry with 9 words
'''
def test_find_best_entry_for_reading_time_three_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry", "one two three")
    diary_entry2 = DiaryEntry("second entry", "one two three four five six")
    diary_entry3 = DiaryEntry("third entry", "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    assert diary.find_best_entry_for_reading_time(5, 2) == diary_entry2

'''
Given 5 wpm and 2 minutes
If all entries are above 10 words
an exception should be raised
'''
def test_find_best_entry_for_reading_time_all_entries_above_time_available():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry", "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen")
    diary_entry2 = DiaryEntry("second entry", "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen")
    diary_entry3 = DiaryEntry("third entry", "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    with pytest.raises(Exception) as err:
        diary.find_best_entry_for_reading_time(5, 2) == "No diary entries can be read in given time"
    error_message = str(err.value)
    assert error_message == "No diary entries can be read in given time"

'''
Given wpm is 0
find_best_entry_for_reading_time should return an error

'''
def test_find_best_entry_for_reading_time_zero_wpm_error():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry", "one two three four five ")
    diary.add(diary_entry1)
    with pytest.raises(Exception) as err:
        diary.find_best_entry_for_reading_time(0, 2) == "No diary entries can be read in given time"
    error_message = str(err.value)
    assert error_message == "Zero cannot be entered"
    
'''
Given minutes is zero
find_best_entry_for_reading_time should return an error
'''

def test_find_best_entry_for_reading_time_zero_wpm_error():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry", "one two three four five ")
    diary.add(diary_entry1)
    with pytest.raises(Exception) as err:
        diary.find_best_entry_for_reading_time(5, 0) == "No diary entries can be read in given time"
    error_message = str(err.value)
    assert error_message == "Zero cannot be entered"
    
'''
Given a phone number exists in the diary entry
#get_contacts should return the phone number
'''
def test_get_contacts_returns_phone_numbers():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry", "one two three four five ")
    diary_entry2 = DiaryEntry("second entry", "It is Thursday and John's number is 07564564564")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.get_contacts() == ["07564564564"]
    

'''
Given multiple phone numbers exists in the diary entries
#get_contacts should return the phone numbers
'''
def test_get_contacts_returns_phone_numbers():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry", "one two three four five ")
    diary_entry2 = DiaryEntry("second entry", "It is Thursday and John's number is 07564564564")
    diary_entry3 = DiaryEntry("second entry", "It is Thursday and joe's number is 07123123123")
    diary_entry4 = DiaryEntry("second entry", "It is Thursday and John's number is 07321321321")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    diary.add(diary_entry4)
    assert diary.get_contacts() == ["07564564564","07123123123","07321321321"]

'''
Given a task is added
todos should contain the task object
'''
def test_add_task_is_in_todos():
    todo_list = TodoList()
    task1 = Todo("Do anything")
    todo_list.add(task1)
    assert todo_list.todos == [task1]
    
'''
Given multiple tasks are added
todos should contain all the task objects
'''
def test_add_multiple_tasks_to_todos_returns_tasks():
    todo_list = TodoList()
    task1 = Todo("Do anything")
    task2 = Todo("Do something")
    todo_list.add(task1)
    todo_list.add(task2)
    assert todo_list.todos == [task1, task2]
    
'''
Given an empty string
#add should return an error "Task is empty"
And todos list shouldn't be populated
'''
def test_add_empty_string_returns_error():
    todo_list = TodoList()
    task1 = Todo("")
    with pytest.raises(Exception) as err:
        todo_list.add(task1)
    error_message = str(err.value)
    assert error_message == "Task is empty"
    
'''
# Given task is not a string
# init should return an error "Only strings can be added"
# '''
def test_wrong_type_added_to_task():
    todo_list = TodoList()
    task1 = Todo(123)
    with pytest.raises(Exception) as err:
        todo_list.add(task1)
    error_message = str(err.value)
    assert error_message == "Only strings can be added"
    
'''
Given todos contains three incomplete tasks
#incomplete should return the three incomplete tasks
'''
def test_todos_contains_three_incomplete_tasks():
    todo_list = TodoList()
    task1 = Todo("Do anything")
    task2 = Todo("Do something")
    task3 = Todo("Do something else")
    todo_list.add(task1)
    todo_list.add(task2)
    todo_list.add(task3)
    assert todo_list.incomplete() == [task1, task2, task3]

'''
Given todo_list.todos contains three incomplete tasks
#diary.get_todo_list should return the three incomplete tasks
'''
def test_get_todo_list_returns_incomplete_tasks():
    diary = Diary()
    todo_list = TodoList()
    task1 = Todo("Do anything")
    task2 = Todo("Do something")
    task3 = Todo("Do something else")
    todo_list.add(task1)
    todo_list.add(task2)
    todo_list.add(task3)
    assert diary.get_todo_list(todo_list) == [task1, task2, task3]
'''
Given a task 
#mark_complete should set the #complete property to True
'''
def test_diary_mark_complete_completes_task():
    diary = Diary()
    todo_list = TodoList()
    task1 = Todo("Do anything") 
    task2 = Todo("Do something")
    todo_list.add(task1)
    todo_list.add(task2)
    diary.complete_todo_list_item(task1)
    assert task1.complete == True
    assert task2.complete == False
    
