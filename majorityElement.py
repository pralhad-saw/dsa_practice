
def find_majority_element(arr):
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
        if count[num] > len(arr) // 2:
            return num
    return None
