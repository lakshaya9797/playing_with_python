# chekcing if file exist.

import os

file_name='student.txt'
 
if os.path.exists(file_name):
    print(f"File {file_name} exists. ")
else:
    print("the file doesn't exists.")

# Renaming the file

if os.path.exists(file_name):
    os.rename("Teacher.txt")
    print("File names successfully.")

# Deleting the file

if os.path.exists(file_name):
    os.remove('Teacher.txt')