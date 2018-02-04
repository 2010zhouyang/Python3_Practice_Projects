class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        robber, not_robber = [nums[0]], [0]
        for i, v in enumerate(nums):
            if i == 0:
                continue
            robber.append(not_robber[i-1] + v)
            not_robber.append(max(robber[i-1], not_robber[i-1]))
            
        return max(robber[-1], not_robber[-1])
