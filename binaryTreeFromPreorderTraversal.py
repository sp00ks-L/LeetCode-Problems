# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    i = 0

    def bstFromPreorder(self, pre, bound=float('inf')):
        '''
        Binary Search Tree:
        - For every node, any descendant of node.left < node.val
        - Any descendant of node.right > node.val

        Preorder traversal: Root -> node.left -> node.right

        Recursively calls to create binary search tree
        - We know root is less than bound (infinity)
        - We can then create the left subtree by using the root as the upper bound
        - The right subtree can be created using infinity as the upper bound
        '''
        if self.i == len(pre) or pre[self.i] > bound:
            return None
        root = TreeNode(pre[self.i])
        self.i += 1
        root.left = self.bstFromPreorder(pre, root.val)
        root.left = self.bstFromPreorder(pre, bound)
        return root
