import re


def assess_password_strength(password):
    """
    Assess the strength of a given password.
    
    Args:
        password (str): The password to evaluate.
    
    Returns:
        dict: A dictionary containing the password score, strength, and feedback.
    """
    # Criteria
    length_score = len(password) >= 12
    uppercase_score = bool(re.search(r"[A-Z]", password))
    lowercase_score = bool(re.search(r"[a-z]", password))
    digit_score = bool(re.search(r"\d", password))
    special_char_score = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    no_common_patterns = not bool(re.search(r"(1234|password|qwerty|letmein|admin|abcdef)", password.lower()))

    # Calculate score
    score = sum([length_score, uppercase_score, lowercase_score, digit_score, special_char_score, no_common_patterns])
    max_score = 6

    # Determine strength
    if score == max_score:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Feedback
    feedback = []
    if not length_score:
        feedback.append("Use at least 12 characters.")
    if not uppercase_score:
        feedback.append("Include at least one uppercase letter.")
    if not lowercase_score:
        feedback.append("Include at least one lowercase letter.")
    if not digit_score:
        feedback.append("Include at least one number.")
    if not special_char_score:
        feedback.append("Include at least one special character.")
    if not no_common_patterns:
        feedback.append("Avoid common patterns like '1234', 'password', or 'qwerty'.")

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback,
    }


# Example usage
if __name__ == "__main__":
    password = input("Enter a password to assess: ")
    result = assess_password_strength(password)
    print(f"\nPassword Strength: {result['strength']}")
    print(f"Score: {result['score']}/6")
    if result['feedback']:
        print("Suggestions:")
        for tip in result['feedback']:
            print(f" - {tip}")
