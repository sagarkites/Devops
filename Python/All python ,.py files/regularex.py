import re
sen = "sagar scott currently learning the python core conpects 1 2 3 5 4"
pattren = re.compile(r'\w')#matching particular string from the above sentence
match = pattren.finditer(sen)#using this we can get index of particular string
for i in match:
    print(i)