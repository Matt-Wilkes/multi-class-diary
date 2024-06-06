import math

class DiaryEntry:
    def __init__(self, title, contents):
        if title == '' or contents == '':
            raise Exception("Title or Content is empty")
        self.title = title
        self.contents = contents
        

    def count_words(self):
        self.entry_length = len(self.contents.split())
        return self.entry_length
  
    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception('No reading time has been entered')
        time_to_read = math.ceil(self.count_words()/wpm)
        return time_to_read 
