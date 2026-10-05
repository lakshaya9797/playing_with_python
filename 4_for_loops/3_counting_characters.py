# Ask the user for a word or phrase, then use a for loop to count how 
# many times the letter "a" (lowercase or uppercase) appears in it.

text = input("Enter a word or phrase: ")
count = 0

for char in text:
    if char.lower() == 'a': #char.lower() == 'a' converts each character to lowercase so it counts both 'a' and 'A'.
        count += 1

print(f"The letter 'a' appears {count} times.")