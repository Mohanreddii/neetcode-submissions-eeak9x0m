class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
       left = 0
       sett = set()
       for right in range(len(nums)):
        if nums[right] in sett:
            return True
        sett.add(nums[right])
        if right-left >= k:
            sett.remove(nums[left])
            left += 1
       return False
        