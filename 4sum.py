 #4 sum using two pointer approach 


def solution(nums):
    nums.sort()
    result = []

    for x in range(len(nums)-3):
        if x > 0 and nums[x] == nums[x-1]:
            continue

        for y in range(x+1, len(nums)-2):
            if y > x+1 and nums[y] == nums[y-1]:
                continue

            left, right = y+1, len(nums)-1

            while left < right:
                total = nums[x] + nums[y] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[x], nums[y], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1

                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

    return result

nums = [1, 0, -1, 0, -2, 2]
print(solution(nums))

#solved 
#just in 4 minutes on manipulating 3sum problem solution 


#complexity analysis 

#Time: O(n³)
# space: O(1)