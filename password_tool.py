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
