def move_zeros_to_end(nums):
    """
    Move all zeros to the end of the array while maintaining the relative order of non-zero elements.

    Args:
        nums (list): The input array of integers.

    Returns:
        list: The modified array with all zeros at the end.
    """
    non_zero_elements = [num for num in nums if num != 0]
    zero_elements = [num for num in nums if num == 0]
    return non_zero_elements + zero_elements

# Example usage:
nums = [0, 1, 0, 3, 12]
result = move_zeros_to_end(nums)
print(result)  # Output: [1, 3, 12, 0, 0]
