import unittest
import BalancedBST as l


class MyTestCase(unittest.TestCase):
    def pre_order(self, node):
        yield node
        if node.LeftChild:
            yield from self.pre_order(node.LeftChild)
        if node.RightChild:
            yield from self.pre_order(node.RightChild)

    def test_GenerateTree(self):
        a = [7, 6, 4, 9, 5, 14, 15, 2, 11, 8, 13, 1, 3, 12, 10]
        bst = l.BalancedBST()
        bst.GenerateTree(a)
        print(bst.IsBalanced(bst.Root))

    def test_balanced(self):
        a = [7, 6, 4, 9, 5, 14, 15, 2, 11, 8, 13, 1, 3, 12, 10]
        bst = l.BalancedBST()
        bst.GenerateTree(a)
        self.assertEqual(bst.IsBalanced(bst.Root), True)
        bst.Root.LeftChild = None
        self.assertEqual(bst.IsBalanced(bst.Root), False)

        a = [7, 6, 4, 9, 5, 14, 15, 2, 11, 8, 13, 1, 3, 12, 10]
        bst = l.BalancedBST()
        bst.GenerateTree(a)

        bst.Root.LeftChild.LeftChild = None
        bst.Root.LeftChild.RightChild = None
        self.assertEqual(bst.IsBalanced(bst.Root), False)

        a = [7, 6, 4, 9, 5, 14, 15, 2, 11, 8, 13, 1, 3, 12, 10]
        bst = l.BalancedBST()
        bst.GenerateTree(a)

        bst.Root.LeftChild.LeftChild.LeftChild = None
        bst.Root.LeftChild.LeftChild.RightChild = None
        self.assertEqual(bst.IsBalanced(bst.Root), True)

        a = [7, 6, 4, 9, 5, 14, 15, 2, 11, 8, 13, 1, 3, 12, 10]
        bst = l.BalancedBST()
        bst.GenerateTree(a)
        bst.Root.RightChild = None
        self.assertEqual(bst.IsBalanced(bst.Root), False)

        a = [7, 6, 4, 9, 5, 14, 15, 2, 11, 8, 13, 1, 3, 12, 10]
        bst = l.BalancedBST()
        bst.GenerateTree(a)

        bst.Root.RightChild.LeftChild = None
        bst.Root.RightChild.RightChild = None
        self.assertEqual(bst.IsBalanced(bst.Root), False)

        a = [7, 6, 4, 9, 5, 14, 15, 2, 11, 8, 13, 1, 3, 12, 10]
        bst = l.BalancedBST()
        bst.GenerateTree(a)

        bst.Root.RightChild.LeftChild.LeftChild = None
        bst.Root.RightChild.LeftChild.RightChild = None
        self.assertEqual(bst.IsBalanced(bst.Root), True)

        a = [7, 6, 4, 9, 5, 14, 15, 2, 11, 8, 13, 1, 3, 12, 10]
        bst = l.BalancedBST()
        bst.GenerateTree(a)
        self.assertEqual(bst.IsBalanced(bst.Root), True)
        bst.Root.LeftChild.RightChild = None
        bst.Root.RightChild = None
        temp1 = l.BSTNode(0, bst.Root.LeftChild.LeftChild.LeftChild)
        temp1.Level = 5
        temp2 = l.BSTNode(1.5, bst.Root.LeftChild.LeftChild.LeftChild)
        temp2.Level = 5
        bst.Root.LeftChild.LeftChild.LeftChild.LeftChild = temp1
        bst.Root.LeftChild.LeftChild.LeftChild.RightChild = temp2
        self.assertEqual(bst.IsBalanced(bst.Root), False)


if __name__ == '__main__':
    unittest.main()