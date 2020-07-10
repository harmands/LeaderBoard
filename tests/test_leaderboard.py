import unittest

from leaderboard import BST, BSTNode, LeaderBoard


def inorder(node):
    def _inorder(node, ans):
        if node is None:
            return

        _inorder(node.left, ans)
        ans.append(node.val)
        _inorder(node.right, ans)
    ans = []
    _inorder(node, ans)
    return ans


class TestBSTNode(unittest.TestCase):

    def test_init(self):

        temp = BSTNode(42)

        self.assertEqual(temp.val, 42)
        self.assertIsNone(temp.left)
        self.assertIsNone(temp.right)
        self.assertEqual(temp.rank, 0)


class TestBST(unittest.TestCase):

    def setUp(self):

        self.test_tree = BST()
        self.test_tree.insert(5)
        self.test_tree.insert(6)
        self.test_tree.insert(3)
        self.test_tree.insert(1)

    def test_insert(self):

        self.assertEqual(self.test_tree.root.val, 5)
        self.assertEqual(self.test_tree.root.rank, 2)

        self.assertEqual(self.test_tree.root.right.val, 6)
        self.assertEqual(self.test_tree.root.right.rank, 0)

        self.assertEqual(self.test_tree.root.left.val, 3)
        self.assertEqual(self.test_tree.root.left.rank, 1)

        self.assertEqual(self.test_tree.root.left.left.val, 1)
        self.assertEqual(self.test_tree.root.left.left.rank, 0)
        self.assertEqual(self.test_tree.root.rank, 2)
        self.assertEqual(self.test_tree.root.left.rank, 1)

    def test_is_bst(self):
        self.assertEqual(inorder(self.test_tree.root), [1, 3, 5, 6])

    def test_search(self):
        self.assertEqual(self.test_tree.search(1), 0)
        self.assertEqual(self.test_tree.search(3), 1)
        self.assertEqual(self.test_tree.search(5), 2)
        self.assertEqual(self.test_tree.search(6), 3)
        self.assertIsNone(self.test_tree.search(9))

    def test_delete(self):
        self.test_tree.delete(3)
        self.assertEqual(inorder(self.test_tree.root), [1, 5, 6])
        self.assertEqual(self.test_tree.search(1), 0)
        self.assertEqual(self.test_tree.search(5), 1)
        self.assertEqual(self.test_tree.search(6), 2)

        self.test_tree.delete(5)
        self.assertEqual(inorder(self.test_tree.root), [1, 6])
        self.assertEqual(self.test_tree.search(1), 0)
        self.assertEqual(self.test_tree.search(6), 1)


class TestLeaderBoard(unittest.TestCase):

    def setUp(self):
        self.lb = LeaderBoard()

    def test_increment(self):
        self.lb.increment(0, 5)
        self.lb.increment(1, 6)
        self.lb.increment(0, 2)

        self.assertEqual(self.lb.user_hash[0], 7)
        self.assertEqual(self.lb.user_hash[1], 6)

    def test_rank_user(self):
        self.lb.increment(0, 5)
        self.lb.increment(1, 6)

        self.assertEqual(self.lb.rank_user(0), 0)
        self.assertEqual(self.lb.rank_user(1), 1)

        self.lb.increment(0, 2)

        self.assertEqual(self.lb.rank_user(0), 1)
        self.assertEqual(self.lb.rank_user(1), 0)
