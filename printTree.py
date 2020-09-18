# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 01:28:34 2020

@author: renli
"""
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class BinaryTree:
    def __init__(self,node=None):
        self.root=node
        self.height=self.getHeight(self.root)
    
    def getHeight(self, root):
        if not root: return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
    
    def printTree(self):
        arr=[[" " for i in range(2**self.height-1)] for j in range(self.height)]
        def dfs(node, layer, index):
            if not node: return
            arr[layer][index] = str(node.val)
            if node.left or node.right:
                dfs(node.left, layer + 1, index - (2**(self.height - layer - 2)))
                dfs(node.right, layer + 1, index + (2**(self.height - layer - 2)))
        dfs(self.root,0,2**(self.height-1)-1)
        for layer in arr:
            print("".join(layer))
        return arr
    
if __name__=="__main__":
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.right=TreeNode(4)
    root.right.left=TreeNode(5)
    root.right.right=TreeNode(6)
    tree=BinaryTree(root)
    res=tree.printTree()