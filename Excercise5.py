<<<<<<< HEAD
#DAY7
"""
create a new file 
write code separately to append and read.
read and append should be in different files
"""
#   1.)
with open('fassignment.txt','w') as f:
    f.write('Hi I am Cherry.\n')
"""
OUTPUT:
A file with fassignment.txt is created and data is stored in that file 
"""
#   2.)
with open('fassignment.txt','a') as f:
    f.write('I am currently in capgemini training.\n')
"""
OUTPUT:
Data is appended into the file of fassignment.txt
"""
#   3.)
import os
print(os.path.abspath('fassignment.txt'))
"""
OUTPUT:
C:\Users\chari\OneDrive\Documents\Python(CapGemini)\Assignment\fassignment.txt
"""
#   4.)
with open('..//text1.txt','r',encoding='utf-8') as f:
    lines= f.readlines()
    print(lines)
"""
OUTPUT:
['Beautiful is better than ugly.\n', '    Explicit is better than implicit.\n', '    Simple is better than complex.\n', 'Explicit is better than implicit.\n', 'Complex is better than complicated.\n', 'Flat is better than nested.\n']
"""
#   5.)
with open('..//renamedfile.txt','r',encoding='utf-8') as f:
    lines= f.readline()
    print(lines)
"""
OUTPUT:
Hello from Python!
=======
#DAY7
"""
create a new file 
write code separately to append and read.
read and append should be in different files
"""
#   1.)
with open('fassignment.txt','w') as f:
    f.write('Hi I am Cherry.\n')
"""
OUTPUT:
A file with fassignment.txt is created and data is stored in that file 
"""
#   2.)
with open('fassignment.txt','a') as f:
    f.write('I am currently in capgemini training.\n')
"""
OUTPUT:
Data is appended into the file of fassignment.txt
"""
#   3.)
import os
print(os.path.abspath('fassignment.txt'))
"""
OUTPUT:
C:\Users\chari\OneDrive\Documents\Python(CapGemini)\Assignment\fassignment.txt
"""
#   4.)
with open('..//text1.txt','r',encoding='utf-8') as f:
    lines= f.readlines()
    print(lines)
"""
OUTPUT:
['Beautiful is better than ugly.\n', '    Explicit is better than implicit.\n', '    Simple is better than complex.\n', 'Explicit is better than implicit.\n', 'Complex is better than complicated.\n', 'Flat is better than nested.\n']
"""
#   5.)
with open('..//renamedfile.txt','r',encoding='utf-8') as f:
    lines= f.readline()
    print(lines)
"""
OUTPUT:
Hello from Python!
>>>>>>> 0d551c5 (Initial commit)
"""