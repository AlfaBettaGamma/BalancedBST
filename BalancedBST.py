class BSTNode:
    
    def __init__(self, key, parent):
        self.NodeKey = key # ключ узла
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.Level = 0 # уровень узла
        
class BalancedBST:
        
    def __init__(self):
        self.Root = None # корень дерева

    def GenerateTree(self, a):
        a.sort()
        tree = []
        def building(parent, a):
            if a:
                node = BSTNode(a[len(a)//2], parent)
                if parent is None:
                    node.Level = 1
                    self.Root = node
                else:
                    node.Level = parent.Level + 1
                tree.append(node)
                node.LeftChild = building(node, a[:len(a)//2])
                node.RightChild = building(node, a[len(a)//2+1:])
            else:
                return None
            return node
        building(None, a)
        return tree
    # создаём дерево с нуля из неотсортированного массива a
    # ...      

    def IsBalanced(self, root_node):
        if root_node is None:
            return True

        def Deep(root):
            if root is None:
                return 0
            return max(Deep(root.LeftChild), Deep(root.RightChild)) + 1
        left_side_tree = Deep(root_node.LeftChild)
        right_side_tree = Deep(root_node.RightChild)
        if abs(left_side_tree - right_side_tree) <= 1 and self.IsBalanced(root_node.LeftChild) is True and self.IsBalanced(root_node.RightChild) is True:
            return True
        return False
        # сбалансировано ли дерево с корнем root_node