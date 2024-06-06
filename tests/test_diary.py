from lib.diary import *
import pytest
'''
Initially
The diary entry is empty
'''
def test_diary_entries_are_empty_initially():
    diary = Diary()
    assert diary.entries == []
