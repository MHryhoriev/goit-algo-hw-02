def is_opening_delimiter(char: str) -> bool:
    """
    Checks if the character is an opening delimiter.
    
    Args:
        char (str): The character to check.

    Returns:
        bool: True if it's an opening delimiter, False otherwise.
    """
    return char in '([{'

def is_closing_delimiter(char: str) -> bool:
    """
    Checks if the character is a closing delimiter.
    
    Args:
        char (str): The character to check.

    Returns:
        bool: True if it's a closing delimiter, False otherwise.
    """
    return char in ')]}'

def matches(opening: str, closing: str) -> bool:
    """
    Checks if the opening and closing delimiters match.
    
    Args:
        opening (str): The opening delimiter.
        closing (str): The closing delimiter.

    Returns:
        bool: True if they match, False otherwise.
    """
    matching_delimiters = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    return matching_delimiters[closing] == opening

def check_delimiters(sequence: str) -> str:
    """
    Checks the symmetry and pairing of delimiters in a given string.
    
    Args:
        sequence (str): The string containing delimiters to check.

    Returns:
        str: A message indicating whether the delimiters are symmetric, unsymmetric,
             or mismatched.
    """
    stack = []

    for char in sequence:
        if is_opening_delimiter(char):
            stack.append(char)
        elif is_closing_delimiter(char):
            if not stack or not matches(stack.pop(), char):
                return f"Mismatched delimiters: found '{char}' without matching."

    if stack:
        return f"Unsymmetric delimiters: unmatched '{stack[-1]}'."
    
    return "Delimiters are symmetric."

def main():
    user_input = input("Enter a sequence of delimiters: ")
    
    result = check_delimiters(user_input)
    print(result)

if __name__ == "__main__":
    main()
