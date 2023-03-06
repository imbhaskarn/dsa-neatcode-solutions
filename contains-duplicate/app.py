class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        myset = set()
        for num in nums:
            if num in myset:
                return True
            myset.add(num)
        return False