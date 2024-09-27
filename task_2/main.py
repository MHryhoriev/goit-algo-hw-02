from collections import deque

def clean_string(input_string: str) -> str:
    """
    Cleans the input string by removing spaces and converting it to lowercase.

    Args:
        input_string (str): The string to clean.

    Returns:
        str: The cleaned string.
    """
    return ''.join(input_string.split()).lower()

def check_palindrome(my_deque: deque) -> bool:
    """
    Checks if the characters in the deque form a palindrome.

    Args:
        my_deque (deque): The deque containing characters to check.

    Returns:
        bool: True if the characters form a palindrome, False otherwise.
    """
    while len(my_deque) > 1:
        if my_deque.popleft() != my_deque.pop():
            return False
    return True

def is_palindrome(input_string: str) -> bool:
    """
    Checks if the given string is a palindrome.

    Args:
        input_string (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    cleaned_string = clean_string(input_string)
    my_deque = deque(cleaned_string)
    return check_palindrome(my_deque)

def main():
    user_input = input("Enter the word or phrase: ")
    print("Palindrom" if is_palindrome(user_input) else "Not a Palindrom")

if __name__ == "__main__":
    main()
