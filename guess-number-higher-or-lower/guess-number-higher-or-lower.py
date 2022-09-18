# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1 : return 1
        
        l , r = 0 , n
        while l <= r:
            mid = int(( l + r)/2)
            
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                r = mid
            else:
                l = mid  + 1
        
        