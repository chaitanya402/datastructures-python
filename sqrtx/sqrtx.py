class Solution:
        
    
    def mySqrt(self, x: int) -> int:
          
            l = 0 
            r = x + 1
            while (l < r):
                mid = int((l + (r-1)) / 2)
                if mid * mid > x :
                    r = mid
                else:
                    l = mid + 1
            return l -1        
            
            
        
        