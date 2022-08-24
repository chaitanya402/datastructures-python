# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            print('p,q',p, q)
            return True
        else:
            if not p:
                print('p',p)
                return False
            if not q:
                print('q',q)
                return False
            print("in here")
            if(p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)):
                print(p.val,q.val)
                return True
            else:
                return False    
        