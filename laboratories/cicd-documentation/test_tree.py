import unittest
from tree import Tree
from node import Node

class TestTreeFind(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        self.tree.add(3)
        self.tree.add(4)
        self.tree.add(0)
        self.tree.add(8)
        self.tree.add(2)

    def test_find_existing_node(self):
        node = self.tree._find(4, self.tree.getRoot())
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 4)

    def test_find_non_existing_node(self):
        node = self.tree._find(10, self.tree.getRoot())
        self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()
