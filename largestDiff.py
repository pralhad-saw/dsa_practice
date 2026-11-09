
def find_largest_difference(arr):
    if len(arr) < 2:
        return None
    min_val = arr[0]
    max_diff = arr[1] - arr[0]
    for num in arr[1:]:
        max_diff = max(max_diff, num - min_val)
        min_val = min(min_val, num)
    return max_diff
