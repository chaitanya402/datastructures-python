# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = [root]
        data = []

        if not root:  return []

        cur = None
        while (len(stack) > 0):
            cur = stack.pop()
            data.append(cur.val)
            if (cur.right):
                stack.append(cur.right)
            if (cur.left):
                stack.append(cur.left)

        return data