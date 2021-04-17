# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.__recursive(root)
    
    def __recursive(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        def _is_leaf(root: TreeNode) -> bool:
            return not (root.left or root.right)

        def _process(root: TreeNode, is_left: bool):

            if _is_leaf(root):
                return root.val if is_left else 0
            
            result = 0

            if root.left:
                result += _process(root.left, is_left=True)
            if root.right:
                result += _process(root.right, is_left=False)

            return result

        return _process(root, is_left=False)

    def __iterative(self, root: TreeNode) -> int:
        ...