# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

       
        self.maxval=float('-inf')
        def traverse(root):
            if not root:
                return 0
                # maxsum+=root.val
                
            leftsum=max(traverse(root.left),0)
            rightsum=max(traverse(root.right),0)
            # print(maxsum,maxval)
            curr_sum=root.val+leftsum+rightsum
            self.maxval=max(curr_sum,self.maxval)

            # maxval=max(maxsum,maxval)
            return root.val + max(leftsum,rightsum)

                
            
        traverse(root)
        return self.maxval


        