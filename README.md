## Python Password Strength Checker & Generator

## Objective
The password project aimed to critically evaluate a password's resilience based on length and character diversity, thereby enhancing security awareness by providing an objective rating from "WEAK" to "VERY STRONG." Additionally, the tool was designed to guide users toward improvement by using a detailed feedback system to clearly instruct on how to strengthen a weak password. Finally, it aimed to ensure cryptographic safety by building a generator that uses the secure secrets module to create passwords, guaranteeing they are complex and resistant to common attacks.

### Skills Learned

The project helped me gain proficiency in several programming and security principles:

- Python Fundamentals.
- Cryptographic Randomness: Applying the secrets module to ensure cryptographically secure random number generation and shuffling.
- Conditional Logic and Control Flow: using if/elif/else structures to determine the final strength rating.
- Algorithmic Design: Implementing a 5-point scoring system for strength quantification and designing a generation algorithm that guarantees complexity requirements.


### Tools Used

- Python 3 served as the core language for all script logic and execution.

- The secrets module was used specifically for providing secure, high-quality randomness.

- The re module was implemented for pattern matching to validate character requirements.

- The string module supplied constants used for defining the required character sets. 

### The Code and Outcomes
 This python code both evaluates the security of user passwords against modern standards and generates highly secure, cryptographically random passwords.
 ```python
import re
import secrets
import string

# --- Configuration ---
MIN_LENGTH = 12
# Define character sets for secure generation
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = string.punctuation
ALL_CHARS = LOWERCASE + UPPERCASE + DIGITS + SYMBOLS

def check_strength(password):
    """
    Evaluates the strength of a given password based on length and character variety.
    
    The score is out of a maximum of 5 points.
    """
    strength_score = 0
    feedback = []

    # 1. Length Check
    if len(password) >= MIN_LENGTH:
        strength_score += 1
        feedback.append("✅ Length requirement met.")
    else:
        feedback.append(f"❌ Password should be at least {MIN_LENGTH} characters long.")

    # 2. Character Type Checks (using Regular Expressions)
    
    # Checks for at least one lowercase letter
    if re.search(r"[a-z]", password):
        strength_score += 1
    else:
        feedback.append("❌ Missing lowercase letter.")

    # Checks for at least one uppercase letter
    if re.search(r"[A-Z]", password):
        strength_score += 1
    else:
        feedback.append("❌ Missing uppercase letter.")

    # Checks for at least one digit
    if re.search(r"\d", password):
        strength_score += 1
    else:
        feedback.append("❌ Missing digit.")

    # Checks for at least one symbol (non-alphanumeric/non-space)
    if re.search(r"[^a-zA-Z0-9\s]", password):
        strength_score += 1
    else:
        feedback.append("❌ Missing symbol.")

    # 3. Final Rating based on Score
    if strength_score == 5:
        rating = "⭐ VERY STRONG (Excellent Complexity)"
    elif strength_score == 4:
        rating = "STRONG (Good Complexity)"
    elif strength_score >= 2:
        rating = "MEDIUM (Needs Improvement)"
    else:
        rating = "WEAK (High Risk)"

    return rating, feedback

def generate_password(length=MIN_LENGTH):
    """
    Generates a cryptographically secure random password.
    
    It ensures the password meets complexity by forcing one of each required type 
    before filling the rest and shuffling.
    """
    if length < 4:
        # A password must be at least 4 characters to guarantee one of each type
        length = 4
    
    # 1. Start with one of each required character type to ensure complexity
    password_list = [
        secrets.choice(LOWERCASE),
        secrets.choice(UPPERCASE),
        secrets.choice(DIGITS),
        secrets.choice(SYMBOLS)
    ]
    
    # 2. Fill the rest of the length with random characters from ALL_CHARS
    for _ in range(length - len(password_list)):
        password_list.append(secrets.choice(ALL_CHARS))

    # 3. Shuffle the list to prevent predictable character order (improves entropy)
    secrets.SystemRandom().shuffle(password_list)

    # 4. Join the list into a final string
    return "".join(password_list)

if __name__ == "__main__":
    print("-" * 50)
    print("       Password Security Tool ")
    print("-" * 50)
    
    # --- 1. Password Generator ---
    PASSWORD_LENGTH = 16
    new_password = generate_password(PASSWORD_LENGTH)
    print(f"\n[GENERATOR MODE]")
    print(f"Generated {PASSWORD_LENGTH}-character Password: \n>> {new_password}")
    
    # Check the strength of the generated password
    rating, _ = check_strength(new_password)
    print(f"Generated Password Strength: {rating}\n")
    
    # --- 2. Password Strength Checker ---
    print("-" * 50)
    user_input = input("Enter a password to check its strength: ")
    
    # Check the strength of the user's input
    rating, feedback = check_strength(user_input)
    
    print(f"\n[CHECKER RESULTS]")
    print(f"Password: '{user_input}'")
    print(f"Rating: {rating}")
    print("\nDetailed Feedback:")
    for item in feedback:
        print(f"  {item}")
```

<img width="647" height="458" alt="weak password" src="https://github.com/user-attachments/assets/9bda4016-4a07-4617-b9e4-33ccdce9fc72" />

Ref 1: Code outcome for weak password



<img width="763" height="372" alt="strongpassword" src="https://github.com/user-attachments/assets/ea8f47f3-2114-4713-882c-dcc74fcfaa9e" />

Ref 2: Code outcome for strong password

### Core Components

1- Password strength checker ( check_strength function):
This component evaluates five criteria
- The length check awards 1 point if the password is 12 characters or longer.
- The character type checks awards 4 points collectively for lowercase, uppercase, digits, and symbols.

2- Secure password generator ( generate_password function):
This component ensures guaranteed complexity by using secrets.SystemRandom(). shuffle() to randomize the order of characters.
