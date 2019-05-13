import unittest

from leaderboard import BST, BSTNode

def inorder(node):
    def _inorder(node, ans)
        if node is None:
            return

        _inorder(node.left)
        ans.append(node.val)
        _inorder(node.right)
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

    def test_insert(self):

        self.test_tree.insert(5)
        self.assertEqual(self.test_tree.root.val, 5)
        self.assertEqual(self.test_tree.root.rank, 0)

        self.test_tree.insert(6)
        self.assertEqual(self.test_tree.root.right.val, 6)
        self.assertEqual(self.test_tree.root.right.rank, 0)

        self.test_tree.insert(3)
        self.assertEqual(self.test_tree.root.left.val, 4)
        self.assertEqual(self.test_tree.root.left.rank, 0)
        self.assertEqual(self.test_tree.root.rank, 1)

        self.test_tree.insert(1)
        self.assertEqual(self.test_tree.root.left.left.val, 1)
        self.assertEqual(self.test_tree.root.left.leftrank, 0)
        self.assertEqual(self.test_tree.root.rank, 2)
        self.assertEqual(self.test_tree.root.left.rank, 1)

    def test_is_bst(self, node, ans):
        self.assertEqual(inorder(self.test_tree.root), [1, 3, 5, 6])

