class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range (0, len(nums), 1):
            a = nums[i]
            nums[i]= a * a

        return sorted(nums)
        