import pytest
from lib.diaryentry import *

'''
Given an empty Title or Contents
An error is raised 
'''
def test_empty_title_or_contents():
    with pytest.raises(Exception) as err:
        DiaryEntry("","")
    error_message = str(err.value)
    assert error_message == "Title or Content is empty"
    

# '''
# When a diary entry is created with a title and contents
# The format attribute returns a formatted title and contents
# "My Title: These are the contents"
# '''

# def test_diary_entry_format():
#     diary_entry = DiaryEntry("Test Driven Development", "Test Driven Development might drive you mad, but before you let it do that, make sure you've written a test")
#     result = diary_entry.format()
#     assert result == "Test Driven Development: Test Driven Development might drive you mad, but before you let it do that, make sure you've written a test"

# '''
# When we call the count_words method
# the number of words in the contents are returned as an int
# '''

# def test_diary_entry_length():
#     diary_entry = DiaryEntry("Test Driven Development", "This is a string for a word count")
#     result = diary_entry.count_words()
#     assert result == 8
    
# '''
# When we call the reading time method and pass in words per minute
# an estimate of the number of minutes (rounded up) to read the content is returned
# '''

# def test_diary_entry_wpm():
#     diary_entry = DiaryEntry("Test Driven Development", "This is a string for a word count")
#     result = diary_entry.reading_time(200)
#     assert result == 1
# '''
# Given a reading time of 0
# an error message should be returned
# '''

# def test_diary_entry_wpm():
#     diary_entry = DiaryEntry("Test Driven Development", "This is a string for a word count")
#     with pytest.raises(Exception) as err:
#         diary_entry.reading_time(0)
#     error_message = str(err.value)
#     assert error_message == 'No reading time has been entered'

    
# '''
# Given a diary content of 15 words
# With a WPM of 2
# And a minutes of 2
# reading chunk returns the first 4 words
# '''
# def test_reading_chunk_two_wpm_two_minutes():
#     diary_entry = DiaryEntry("Test Driven Development", "In a small town nestled between rolling hills and dense forests, there lived a rabbit")
#     result = diary_entry.reading_chunk(2, 2) 
#     assert result == "In a small town"
    
# '''
# Given a diary content of 15 words
# With a WPM of 2
# And a minutes of 4
# #reading_chunk returns the first 8 words
# '''
# def test_reading_chunk_two_wpm_four_minutes():
#     diary_entry = DiaryEntry("Test Driven Development", "In a small town nestled between rolling hills and dense forests, there lived a rabbit")
#     result = diary_entry.reading_chunk(2, 4) 
#     assert result == "In a small town nestled between rolling hills"

# '''
# Given a contents of 15 words
# And a wpm of 2 and a 2 minutes
# first time #reading_chunk returns "In a small town"
# next time #reading_chunk returns "nestled between rolling hills"
# next time #reading_chunk returns "and dense forests, there"
# '''

# def test_reading_chunk_two_wpm_and_two_minutes_called_three_times():
#     diary_entry = DiaryEntry("Test Driven Development", "In a small town nestled between rolling hills and dense forests, there lived a rabbit")
#     assert diary_entry.reading_chunk(2, 2) == "In a small town"
#     assert diary_entry.reading_chunk(2, 2) == "nestled between rolling hills"
#     assert diary_entry.reading_chunk(2, 2) == "and dense forests, there"

# '''
# Given a contents of 15 words
# And a wpm of 2 and a 2 minutes
# first time #reading_chunk returns "In a small town"
# next time with a wpm of 2 and 1 minutes #reading_chunk returns "nestled between"
# next time with a wpm of 2 and 2 minutes #reading_chunk returns "rolling hills and dense"
# '''

# def test_reading_chunk_two_wpm_and_two_minutes_called_three_times():
#     diary_entry = DiaryEntry("Test Driven Development", "In a small town nestled between rolling hills and dense forests, there lived a rabbit")
#     assert diary_entry.reading_chunk(2, 2) == "In a small town"
#     assert diary_entry.reading_chunk(2, 1) == "nestled between"
#     assert diary_entry.reading_chunk(2, 2) == "rolling hills and dense"
   
# ''' 
# Given a contents of 15 words
# And a wpm of 2 and 3 minutes
# if #reading_chunk is called repeatedly
# the last chunk is the last words in the text even if shorter than words that can be read
# the next chunk after that is the start of the chunk again
# '''

# def test_reading_chunk_with_multiple_calls_wraps_correctly():
#     diary_entry = DiaryEntry("Test Driven Development", "In a small town nestled between rolling hills and dense forests, there lived a rabbit")
#     assert diary_entry.reading_chunk(2, 3) == "In a small town nestled between"
#     assert diary_entry.reading_chunk(2, 3) == "rolling hills and dense forests, there"
#     assert diary_entry.reading_chunk(2, 3) == "lived a rabbit"
#     assert diary_entry.reading_chunk(2, 3) == "In a small town nestled between"

# ''' 
# Given a contents of 15 words
# And a wpm of 5 and 1 minutes
# if #reading_chunk is called repeatedly
# and the last chunk equals the last words in the text
# the next chunk should be the first chunk again
# '''

# def test_reading_chunk_wraps_around_after_multiple_calls():
#     diary_entry = DiaryEntry("Test Driven Development", "In a small town nestled between rolling hills and dense forests, there lived a rabbit")
#     assert diary_entry.reading_chunk(5, 1) == "In a small town nestled"
#     assert diary_entry.reading_chunk(5, 1) == "between rolling hills and dense"
#     assert diary_entry.reading_chunk(5, 1) == "forests, there lived a rabbit"
#     assert diary_entry.reading_chunk(5, 2) == "In a small town nestled between rolling hills and dense"