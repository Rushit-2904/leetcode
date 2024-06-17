from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if count == 0 or nums[count - 1] != i:
                nums[count] = i
                count += 1
        return count