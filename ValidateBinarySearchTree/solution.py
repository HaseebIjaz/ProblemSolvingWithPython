# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The solution  fails a few test cases and only validated a single node
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
        

class Solution1:
    def isValidBST(self, root:Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        nodes_to_visit = [root]
        low_high_limits = [{"low":None, "high":None}]

        while nodes_to_visit:
            current_node = nodes_to_visit.pop(0)
            current_pair = low_high_limits.pop(0)

            if current_pair["low"] is not None:
                if current_node.val <= current_pair["low"]:
                    return False
                
            if current_pair["high"] is not None:
                if current_node.val >= current_pair["high"]:
                    return False
            
            if current_node.left is not None:
                if current_node.val <= current_node.left.val:
                    return False
                else:
                    nodes_to_visit.append(current_node.left)
                    low_high_limits.append({"low": current_pair["low"],"high": current_node.val})

            if current_node.right is not None:
                if current_node.val <= current_node.right.val:
                    return False
                else:
                    nodes_to_visit.append(current_node.right)
                    low_high_limits.append({"low": current_node.val, "high": current_pair.high})
            
        return True

