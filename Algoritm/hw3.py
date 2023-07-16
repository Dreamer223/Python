class RedBlackNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = "RED"  # Новые ноды всегда красные


class RedBlackTree:
    def __init__(self):
        self.root = None

    def left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left

        if right_child.left is not None:
            right_child.left.parent = node

        right_child.parent = node.parent

        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right

        if left_child.right is not None:
            left_child.right.parent = node

        left_child.parent = node.parent

        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child

    def insert(self, key):
        new_node = RedBlackNode(key)
        self._insert_node(new_node)
        self._balance_tree_after_insertion(new_node)

    def _insert_node(self, node):
        current_node = None
        temp_node = self.root

        while temp_node is not None:
            current_node = temp_node
            if node.key < temp_node.key:
                temp_node = temp_node.left
            else:
                temp_node = temp_node.right

        node.parent = current_node

        if current_node is None:
            self.root = node
        elif node.key < current_node.key:
            current_node.left = node
        else:
            current_node.right = node

    def _balance_tree_after_insertion(self, node):
        while node.parent is not None and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                if uncle is not None and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)

                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left

                if uncle is not None and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)

                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.left_rotate(node.parent.parent)

        self.root.color = "BLACK"

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(f"Key: {node.key}, Color: {node.color}")
            self.inorder_traversal(node.right)


# Пример использования

tree = RedBlackTree()

tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)
tree.insert(54)
tree.insert(59)

tree.inorder_traversal(tree.root)
