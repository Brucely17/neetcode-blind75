# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not  root:
            return []

        queue=[]
        queue.append(root)
        
        # res=[[root.val]]
        res=[]
        while queue:
            # temp=queue.pop(0)
            arr=[]
            for i in range(len(queue)):
                a=queue.pop(0)
                arr.append(a.val)
            
                l=a.left
                r=a.right
                if l:
                    queue.append(l)
                if r:
                    queue.append(r)
            res.append(arr)
                # print(temp.val,l.val,r.val,'\n')
        return res