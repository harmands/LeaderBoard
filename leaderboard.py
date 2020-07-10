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

    def _search(self, node, val, rank):

        if node is None:
            return None
        if node.val == val:
            return rank + node.rank
        if node.val < val:
            return self._search(node.right, val, rank + node.rank + 1)
        else:
            return self._search(node.left, val, rank)

    def _delete(self, node, val):
        if node.val == val:
            if not node.left and not node.right:
                return None
            elif not node.left or not node.right:
                return node.left or node.right
            else:
                prev = node.left
                while prev.right:
                    prev = prev.right
                node.val = prev.val
                node.left = self._delete(node.left, prev.val)
                node.rank -= 1
                return node
        else:
            if node.val < val:
                node.right = self._delete(node.right, val)
            else:
                node.rank -= 1
                node.left = self._delete(node.left, val)
            return node

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def search(self, val):
        return self._search(self.root, val, 0)


class LeaderBoard(object):

    def __init__(self):
        self.user_hash = {}
        self.rank_tree = BST()

    def increment(self, user, points):
        if user not in self.user_hash:
            self.user_hash[user] = points
        else:
            self.rank_tree.delete((self.user_hash[user], user))
            self.user_hash[user] += points
        self.rank_tree.insert((self.user_hash[user], user))

    def rank_user(self, user):
        if user not in self.user_hash:
            return False
        return self.rank_tree.search((self.user_hash[user], user))
