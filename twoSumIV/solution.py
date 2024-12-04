# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        nodesToVisit = [root]
        visited_values_hash_set = set()
        while nodesToVisit:
            current_node = nodesToVisit.pop(0)
            complement = k - current_node.val
            if complement in visited_values_hash_set:
                return True
            visited_values_hash_set.add(current_node.val)
            if current_node.left:
                nodesToVisit.append(current_node.left)
            if current_node.right:
                nodesToVisit.append(current_node.right)
        return False

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        nodes_to_visit = [root]
        visited_values_hash_set = set()
        while nodes_to_visit:
            current_node = nodes_to_visit.pop(0)
            complement = k - current_node.val
            if complement in visited_values_hash_set:
                return True
            visited_values_hash_set.add(current_node.val)
            if current_node.left:
                nodes_to_visit.append(current_node.left)
            if current_node.right:
                nodes_to_visit.append(current_node.right)
        return False

        
class Solution:
    def findTarget(self, root: Optional[TreeNode], k:int) -> bool:
        if root is None:
            return False
        nodes_to_visit = [root]
        visited_values_hash_set = set()
        while nodes_to_visit:
            current_node = nodes_to_visit.pop(0)
            complement = k - current_node.val
            if complement in visited_values_hash_set:
                return True
            visited_values_hash_set.add(current_node.val)
            if current_node.left:
                nodes_to_visit.append(current_node.left)
            if current_node.right:
                nodes_to_visit.append(current_node.right)
        return False

            
class Solution:
    def findTarget(self, root: Optional[TreeNode], k:int) -> bool:
        if root is None:
            return False
        nodes_to_visit = [root]
        visited_nodes_hash_set = set()
        while nodes_to_visit:
            current_node = nodes_to_visit.pop(0)
            complement = k - current_node.val
            if complement in visited_nodes_hash_set:
                return True
            visited_nodes_hash_set.add(current_node.val)
            if current_node.left:
                nodes_to_visit.append(current_node.left)
            if current_node.right:
                nodes_to_visit.append(current_node.right)
        return False