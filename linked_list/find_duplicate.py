def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]  # Move slow one step
        fast = nums[nums[fast]]  # Move fast two steps
        if slow == fast:
            break

    # Step 2: Find the entrance to the cycle (duplicate number)
    slow = nums[0]  # Reset slow to the start of the list
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return fast  # The duplicate number


# Example usage
nums = [7, 1, 5, 6, 8, 4, 2, 3, 9, 4]
print(findDuplicate(nums))  # Output: 3
