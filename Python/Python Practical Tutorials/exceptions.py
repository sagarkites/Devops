#!usr/bin/python
try:
    7/0
except: #to raise an error
    print('zero division error')
else: #if error was not occur
    print('fuck you')
finally: #even error was occur it executes
    print('everything is okay')
