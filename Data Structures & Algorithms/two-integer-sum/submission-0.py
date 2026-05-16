class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reminder = {}
        for i in range(len(nums)):
            if nums[i] in reminder:
                return [reminder[nums[i]],i]
            needed = (target-nums[i])
            reminder[needed]= i
        return []