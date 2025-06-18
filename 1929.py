class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans= [] * len(nums)
        for i in range (0,2):
            for j in range(0, len(nums)):
                ans.append(nums[j])

        return ans

        