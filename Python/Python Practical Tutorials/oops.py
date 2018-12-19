#!usr/bin/python3
class Physcolgist:

     def __init__(self): #intialization
         self.name = 'sherlock homes' #attributes
         self.eyes_color = 'blue'

     def work(self): #functions to do something with attributes       
         return "{} is with {} eyes highly intrested in the chemistry".format(self.name, self.eyes_color)

sherlock_homes = Physcolgist() #instance or object
print(sherlock_homes.name) #what to printed
print(sherlock_homes.eyes_color)
print(sherlock_homes.work()) # To use function in oops

