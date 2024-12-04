# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        nodes_to_visit = [root]
        while nodes_to_visit:
            current_node: TreeNode = nodes_to_visit.pop(0)
            if current_node.left is not None:
                if current_node.val <= current_node.left.val:
                    return  False
                else:
                    nodes_to_visit.append(current_node.left)
            if current_node.right is not None:
                if current_node.val >= current_node.right.val:
                    return False
                else:
                    nodes_to_visit.append(current_node.right)
        return True
        