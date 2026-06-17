class ConsoleLogger:
    def log(self,message):
        print(message)
        
class TextFileLogger:
    def __init__(self,file_object):
        self.file_object = file_object

    def log(self,message):
        self.file_object.write(message.strip())
        self.file_object.write("\n")
        self.file_object.flush()

class CSVLogger:
    def __init__(self,file_object):
        self.file_object = file_object

    def log(self, message):
        words = message.split()
        from csv import writer
        csv_writer = writer(self.file_object)
        csv_writer.writerow(words)
        self.file_object.flush()
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------------


class FilteredConsoleLogger(ConsoleLogger):
    def __init__(self, pattern):
        self.pattern = pattern
    
    # overriding the log method present in Parent class
    def log(self, message):
        if self.pattern in message:     # adding extra functionality (filtering the messages)
            super().log(message)    # reusing the existing functionality of parent class

class FilteredTextFileLogger(TextFileLogger):
    def __init__(self, pattern, file_object):
        self.pattern = pattern
        super().__init__(file_object)
    
    def log(self, message):
        if self.pattern in message:
            super().log(message)

class FilteredCSVLogger(CSVLogger):
    def __init__(self, pattern, file_object):
        self.pattern = pattern
        super().__init__(file_object)
    
    def log(self, message):
        if self.pattern in message:
            super().log(message)        
        
        
