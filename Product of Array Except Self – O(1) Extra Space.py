# Product of Array Except Self – O(1) Extra Space

def solution(nums):
    n = len(nums)
    result = [1] * n

    # First pass: Prefix products
    for i in range(1, n):
        result[i] = result[i-1] * nums[i-1]

    # Second pass: Suffix products
    suffix = 1
    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result
