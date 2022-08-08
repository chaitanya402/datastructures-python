class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
         mem = {}
            
         def backtrack(i,sum):
            if i == len(nums) :
                return 1 if sum == target else 0
            
            if (i,sum) in mem: return mem[(i,sum)]
            
            mem[(i,sum)] = (backtrack(i+1 , sum + nums[i]) + backtrack(i+1 , sum - nums[i]))
            return mem[(i,sum)]
        
        
         return backtrack(0,0)   
            
                
            
        
            
        
        