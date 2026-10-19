a='sheetal'
b='ankita'

with open("text_for_python.txt","r") as file:
   book=file.read()
   copy=file.readline()
   device=file.readlines()

print(book)
print(copy)
print(device)


# with open("text_for_python.txt", "r") as file:
#     # Read the first line
#     line1 = file.readline()
#     # Read the second line
#     line2 = file.readline()
    
# print("First line:", line1)
# print("Second line:", line2)

# print("First line:", line1.strip())
# print("Second line:", line2.strip())
