# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def traverse(root,p,q):
            if root:
                
                if p.val<=root.val and q.val>=root.val or p.val>=root.val and q.val<=root.val:
                    
                    return root
                elif p.val<=root.val and q.val<=root.val:
                    


                    return traverse(root.left,p,q)
                elif p.val>=root.val and q.val>=root.val:
                    
                    return traverse(root.right,p,q)
            
                
                
                
        return traverse(root,p,q)