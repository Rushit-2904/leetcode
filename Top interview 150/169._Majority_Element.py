from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = value = 0
        for i in nums:
            if count == 0:
                value = i
            if value!=i:
                count -= 1
            else:
                count += 1
        return value
    
if __name__ == "__main__":
    solution = Solution()
    input_values = [
        [3,2,3],
        [2,2,1,1,1,2,2],
        [9,4,9,2,9,5,7,8,9,1],
    ]
    expected_output = [3,2,9]
    actual_output = []
    for i in input_values:
        count = solution.majorityElement(i)
        actual_output.append(count)    
    for actual,expected in zip(actual_output,expected_output):
        assert actual == expected, "All test cases have been passed"