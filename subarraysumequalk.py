def subarraySum(nums, k):
    prefix_map = {0: 1}
    curr_sum = 0
    count = 0
    
    for num in nums:
        curr_sum += num
        # Check if there is a prefix sum that makes up the difference
        if (curr_sum - k) in prefix_map:
            count += prefix_map[curr_sum - k]
        
        # Record the current prefix sum frequency
        prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1
        
    return count
