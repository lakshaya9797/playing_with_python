# Program: Saving a user's profile information
username = "Alex99"
joined_year = 2026

# "w" opens the file for writing. It creates 'user_profile.txt' if it doesn't exist.
with open("text_for_python.txt", "w") as file:
    # .write() requires strings, and we add \n manually for a line break
    file.write(f"Username: {username}\n")
    file.write(f"Joined Year: {joined_year}\n")
    file.write("Ashok")

print("Profile saved successfully!")