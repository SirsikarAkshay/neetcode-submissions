# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def traverse(self, root, tree):
        if root == None:
            tree.append("#")
            return 
        tree.append(root.val)
        self.traverse(root.left, tree)
        self.traverse(root.right, tree)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        root_list = list()
        subroot_list = list()

        self.traverse(root, root_list)
        self.traverse(subRoot, subroot_list)

        rt = "".join(str(r) for r in root_list)
        srt = "".join(str(sr) for sr in subroot_list)

        print(rt)
        print(srt)
        return srt in rt