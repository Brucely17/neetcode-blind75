# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


            def isSame(root,subroot):
                if root is None and subroot is None:
                    return True
                if root is  None or subroot is None:
                    return False
                return root.val==subroot.val and isSame(root.left,subroot.left) and isSame(root.right,subroot.right)
            def traverse(root,subroot):
                if root:
                    
                    
                    print(root,'\n',subroot,'\n\n')
                    traverse(root.left,subroot)
                    traverse(root.right,subroot)
                    if isSame(root,subroot):
                        print(True)
                        return True
                    traverse(root.left,subroot)
                    traverse(root.right,subroot)
                else:
                    return False
                
                    
            return traverse(root,subRoot)
            



                    
                
                    
        