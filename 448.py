class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            index = abs(num) - 1  # map value to index
            if nums[index] > 0:
                nums[index] = -nums[index]  # mark as seen

        # Collect numbers not marked (i.e., still positive)
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
