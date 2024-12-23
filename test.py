def check_unique_elements(lst):
    """
    Checks if all elements in the list are unique.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: True if all elements are unique, False otherwise.
    """
    return len(lst) == len(set(lst))

# Example usage:
numbers = [1, 2, 3, 4, 5]
print(check_unique_elements(numbers))  # Output: True

numbers = [1, 2, 2, 3, 4]
print(check_unique_elements(numbers))  # Output: False