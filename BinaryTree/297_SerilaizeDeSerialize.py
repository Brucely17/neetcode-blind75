# Hard prob

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.s=''
        def traverse(root):
            if root:
                # self.s+='#'+str(root.val)
                self.s+='#'+str(root.val)
                traverse(root.left)
                traverse(root.right)
            else:
                self.s+='#'+str(None)
                return
        traverse(root)
        print(self.s)
        return self.s
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
       
        x=data.split("#")
        x=x[1:]

        self.i=0
        def preorder():
            if x[self.i]=='None':
                self.i+=1
                return None
            node=TreeNode(int(x[self.i]))
            self.i+=1
            node.left=preorder()
            node.right=preorder()
            return node
        
        return preorder()




