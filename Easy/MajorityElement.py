class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate, counter = nums[0], 0
        for i in nums:
            if counter == 0:
                candidate = i
                counter = 1
            elif candidate == i:
                counter += 1
            else:
                counter -= 1
        return candidate