#!usr/bin/python3 

def add(num):
    return num + 2
print(list(map(add, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))) # map needs fun and sequence, it should be converted to another data type to print output
