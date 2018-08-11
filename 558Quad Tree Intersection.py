"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if quadTree1 is None:
            return quadTree2
        if quadTree2 is None:
            return quadTree1
        if quadTree1.isLeaf and quadTree2.isLeaf:
            return Node(quadTree1.val or quadTree2.val, True, None, None, None, None)
        quad = Node(False, False, None, None, None, None)
        if quadTree1.isLeaf and not quadTree2.isLeaf:
            quad.topLeft = self.intersect(quadTree1, quadTree2.topLeft)
            quad.topRight = self.intersect(quadTree1, quadTree2.topRight)
            quad.bottomLeft = self.intersect(quadTree1, quadTree2.bottomLeft)
            quad.bottomRight = self.intersect(quadTree1, quadTree2.bottomRight)
            
        elif not quadTree1.isLeaf and quadTree2.isLeaf:
            quad.topLeft = self.intersect(quadTree1.topLeft, quadTree2)
            quad.topRight = self.intersect(quadTree1.topRight, quadTree2)
            quad.bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2)
            quad.bottomRight = self.intersect(quadTree1.bottomRight, quadTree2)
            
        else:
            quad.topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            quad.topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
            quad.bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
            quad.bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
            
        if quad.topLeft.val and quad.topRight.val and quad.bottomLeft.val and quad.bottomRight.val:
            quad.val = True
            quad.topLeft = None
            quad.topRight = None
            quad.bottomRight = None
            quad.bottomLeft = None
            quad.isLeaf = True
        return quad
