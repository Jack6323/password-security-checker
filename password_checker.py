
import string

# Request users input of their password
password = input("Enter your password: ")

# Checks to see whether conditions are met within password
good_length = len(password) >= 8
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_number = any(c.isdigit() for c in password)
has_symbol = any(c in string.punctuation for c in password)


# Sets password score to 0
score = 0

# Checks to see if password fits requirements and adds score if it does
if good_length:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_number:
    score += 1
if has_symbol:
    score += 1

# List of commonly used passwords
common_passwords = ["password", "123456", "qwerty", "admin", "letmein", "12345678","87654321","11111111"]

# Identifies weak, frequently used passwords, instantly assigning a score of 0 and providing feedback
if password.lower() in common_passwords:
    print("This is a commonly used very weak password!")
    score = 0

# Creates a list for suggestions
suggestions = []

# If password does not meet requirements it adds a reccomendation of what is missing too suggestions list
if not good_length:
    suggestions.append("at least 8 characters")
if not has_upper:
    suggestions.append("an uppercase letter")
if not has_lower:
    suggestions.append("a lowercase letter")
if not has_number:
    suggestions.append("a number")
if not has_symbol:
    suggestions.append("a special character")
    
print("\nPassword Feedback:\n")    

# Informs user how strong their password is based off the scoring system
if score == 5:
    print("Very Strong Password!")
elif score >= 4:
    print("Strong Password!")
elif score >= 3:
    print("Moderate Password!")
else:
    print("Weak Password!")

# Uses the suggestions list to let you know what could be improve in your password. Also lets you know if there are no issues
if suggestions:
    print("\nImprove your password by adding:", ", ".join(suggestions))
else:
    print("\nYour password meets all the security requirements.")

