class Solution(object):
    def maxSubArray(self, nums):
        currentSum = nums[0]
        maxSum = nums[0]

        for num in nums[1:]:
            currentSum = max(currentSum + num, num)

            if currentSum > maxSum:
                maxSum = currentSum

        return maxSum