class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,nums in enumerate(nums):
            if target - nums in dic:
                return [dic[target - nums],i]
            dic[nums] = i