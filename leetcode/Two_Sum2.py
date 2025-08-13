class Solution(object):
    def twoSum(self, nums, target):
        hasht = {}
        for i in range(0,len(nums)):
            res = target - nums[i]

            if res in hasht:
                return [hasht[res],i]
        
            hasht[nums[i]] = i