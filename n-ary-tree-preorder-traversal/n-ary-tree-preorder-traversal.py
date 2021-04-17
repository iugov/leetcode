"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        return self._top_down(root, [])

    def _bottom_up(self, root: 'Node') -> List[int]:
        result = []

        if root:
            result.append(root.val)
            for child in root.children:
                result.extend(self.preorder(child))

        return result
    
    def _top_down(self, root: 'Node', result) -> List[int]:
        if not root:
            return

        result.append(root.val)

        for child in root.children:
            self._top_down(child, result)

        return result