from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if count == 0 or count == 1 or nums[count - 2] != i:
                nums[count] = i
                count += 1
        return count