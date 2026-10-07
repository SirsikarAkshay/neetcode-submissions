# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root, tree):
        if root == None:
            tree.append(0)
            return
            
        tree.append(root.val)
        self.traverse(root.left, tree)
        self.traverse(root.right, tree)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        t1 = list()
        t2 = list()

        self.traverse(p, t1)
        self.traverse(q, t2)

        return t1 == t2