
# //problem statement

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000


4 approaches


# 1. [Naive Approach] Using Triple Nested Loops - O(n × n × m) Time and O(1) Space

def intersect(a, b):
    res = []

    # Traverse through a[] and 
    # search every element a[i] in b[]
    for i in a:
        for j in b:
          
            # If found, check if the element
            # is already in the result
            if i == j and i not in res:
                res.append(i)
                
    return res

if __name__ == "__main__":
    a = [1, 2, 3, 2, 1]
    b = [3, 2, 2, 3, 3, 2]

    res = intersect(a, b)

    print(" ".join(map(str, res)))


# 2. [Better Approach] Using Nested Loops and Hash Set - O(n × m) Time and O(n) Space


