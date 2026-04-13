class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
            max_lst = []
            left = 0
            right = 0
            while right <=len(nums)-k:
                window = nums[right:right+k]
                max_lst.append(max(window))
                
                right+=1
            return max_lst