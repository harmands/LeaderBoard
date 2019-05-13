class BSTNode():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.rank = 0


class BST(object):

    def __init__(self):
        self.root = None

    def _insert(self, node, val):
        if not node:
            return BSTNode(val)
        if node.val < val:
            node.right = self._insert(node.right, val)
        else:
            node.rank += 1
            node.left = self._insert(node.left, val)
        return node

    def insert(self, val):
        self.root = self._insert(self.root, val)


class LeaderBoard(self):
    pass
