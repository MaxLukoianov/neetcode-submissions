class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = defaultdict(int)
        for i in range(len(nums)):
            counter[nums[i]] += 1
            if counter[nums[i]] > 1:
                return True
        return False