# Python
def find_max_avg(nums, k):
    if len(nums) < k:
        return None
    window_sum = sum(nums[:k])
    max_avg = window_sum / k
    # Slide the window across the array.
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_avg = max(max_avg, window_sum / k)
    return max_avg

if __name__ == '__main__':
    print(find_max_avg(nums=[1, 12, -5, -6, 50, 3], k=4))
