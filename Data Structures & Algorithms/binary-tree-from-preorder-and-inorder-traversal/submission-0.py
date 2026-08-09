# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTreeRecu(self, mp, preorder, preIndex, left, right):
        if left > right:
            return None
        
        rootVal = preorder[preIndex[0]]
        preIndex[0] += 1

        index = mp[rootVal]

        root = TreeNode(rootVal)

        root.left = self.buildTreeRecu(mp, preorder, preIndex, left, index-1)
        root.right = self.buildTreeRecu(mp, preorder, preIndex, index+1, right) 

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIndex = [0]
        mp = {value: i for i, value in enumerate(inorder)}

        return self.buildTreeRecu(mp, preorder, preIndex, 0, len(inorder) - 1)
    
    
        