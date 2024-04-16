import string
import secrets

def generate_password(length, character_sets):
    """
    Generate a secure password with the specified length and character requirements.

    Args:
        length (int): The desired length of the password.
        character_sets (list): A list of character sets to include in the password.

    Returns:
        str: The generated password.
    """
    characters = ''.join(character_sets)
    
    if not characters:
        return "Error: No character types selected."

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password
def get_strength_rating(password, min_length=8, special_chars=string.punctuation):
    """
    Determine the strength rating of the given password.

    Args:
        password (str): The password to check.
        min_length (int): The minimum length required for a strong password.
        special_chars (str): The string of special characters to consider.

    Returns:
        str: A string indicating the password strength ("Weak", "Medium", "Medium+", "Strong").
    """
    strength_ratings = ["Weak", "Weak", "Medium", "Medium+", "Strong"]
    criteria_met = sum((
        len(password) >= min_length,
        any(char.isupper() for char in password),
        any(char.islower() for char in password),
        any(char.isdigit() for char in password),
        any(char in special_chars for char in password)
    ))
    return strength_ratings[min(criteria_met, len(strength_ratings) - 1)]
    
def main():
    print("Welcome to the Password Generator!")
    print("This script will generate secure passwords based on your requirements.")

    length = int(input("Enter the desired password length (minimum 8): "))
    if length < 8:
        print("Warning: Password length should be at least 8 characters for better security.")

    character_types = {
        "uppercase": string.ascii_uppercase,
        "lowercase": string.ascii_lowercase,
        "digits": string.digits,
        "special_chars": string.punctuation
    }

    character_sets = []
    for name, chars in character_types.items():
        include = input(f"Include {name}? (y/n): ").lower() == 'y'
        if include:
            character_sets.append(chars)

    num_passwords = int(input("Enter the number of passwords to generate: "))

    for _ in range(num_passwords):
        password = generate_password(length, character_sets)
        if password.startswith("Error"):
            print(password)
        else:
            strength = get_strength_rating(password)
            print(f"Generated password: {password} (Strength: {strength})")

if __name__ == "__main__":
    main()
