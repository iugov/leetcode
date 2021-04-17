"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        return self._bottom_up(root)

    def _bottom_up(self, root: 'Node') -> List[int]:
        result = []

        if root:
            
            for child in root.children:
                result.extend(self._bottom_up(child))
            
            result.append(root.val)

        return result
    
    def _top_down(self, root: 'Node', result) -> List[int]:
        if root:
            
            for child in root.children:
                self._top_down(child, result)
            
            result.append(root.val)

        return result