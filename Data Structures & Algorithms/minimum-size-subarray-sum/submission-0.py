class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        left = 0 
        max_sum = 0
        w_len = 0
        for right in range(len(nums)):
            max_sum += nums[right]
            
            while max_sum >= target:
            
                min_len = min(min_len,right-left+1)
                print("W_len:",w_len)
                max_sum = max_sum-nums[left]
                left += 1
            
        if min_len == float("inf"):
            min_len = 0
        return min_len  