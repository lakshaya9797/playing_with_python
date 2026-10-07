# Ask the user for a word or phrase, then use a for loop to count how 
# many times a vowerl (lowercase or uppercase) appears in it.

text = input("Enter a word or phrase: ")
count = 0

for char in text:
    if char.lower() == 'a' or char.lower()=='e'or char.lower()=='i'or char.lower()=='o'or char.lower()=='u': #char.lower() == 'a' converts each character to lowercase so it counts both 'a' and 'A'.
        count += 1

print(f"Vowerls appeared {count} times.")