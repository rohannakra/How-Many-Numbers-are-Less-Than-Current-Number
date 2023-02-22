# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

def smaller(nums):
    counts = []

    for i in range(len(nums)):
        selected = nums[i]
        counts.append(0)
        for other in nums[:i] + nums[i+1:]:
            if other < selected:
                counts[-1] += 1
    
    return counts

print(smaller([6, 5, 4, 8]))
print(smaller([7, 7, 7, 7]))
print(smaller([8, 1, 2, 2, 3]))

# -------------------------------------------------------------------------------------------

# Accepted LeetCode Solution:

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = []

        for i in range(len(nums)):
            selected = nums[i]
            counts.append(0)
            for other in nums[:i] + nums[i+1:]:
                if other < selected:
                    counts[-1] += 1
    
        return counts
