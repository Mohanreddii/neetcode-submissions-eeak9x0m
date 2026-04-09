class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        left = 0 
        window_sum = 0
        w_len = 0
        for right in range(len(nums)):
            window_sum += nums[right]
            
            while window_sum >= target:
            
                min_len = min(min_len,right-left+1)
                window_sum -= nums[left]
                left += 1
            
        return 0 if min_len == float("inf")  else min_len