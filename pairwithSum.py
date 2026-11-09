
def find_pair_with_sum(arr, target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return (target - num, num)
        seen.add(num)
    return None
