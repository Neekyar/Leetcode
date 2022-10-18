class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = sum(nums[:3])
        n = len(nums)
        for i in range (n):
            j, k = i+1, n-1
            while j < k:
                nsum = nums[i] + nums[j] + nums[k]
                if nsum == target:
                    return nsum
                
                if abs(nsum - target) < abs(result - target):
                    result = nsum
                
                if nsum < target:
                    j += 1
                elif nsum > target:
                    k -= 1
                    
        return result
