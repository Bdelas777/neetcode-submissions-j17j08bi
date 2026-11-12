class Solution:
    def productExceptSelf(self, nums):
        

        res =  [1] * len(nums)
        #[1,1,1,1]
        #[1,2,4,6]
        for i in range(1, len(nums)):
            res[i] = nums[i - 1] * res[i-1]
        #[1,1,2,8]
        #[48,24,12,8]
        postfix = 1 
        # 6
        for j in range(len(nums)-1, -1 , -1):
            res[j] *= postfix
            postfix *= nums[j]
        return res
        