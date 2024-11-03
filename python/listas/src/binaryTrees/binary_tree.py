from node import Node

class Binary:

    def __init__(self):
        self.root = None


    def is_empty(self, node):
        return node is None


    def insert(self, value, node=None):
        if self.is_empty(node):
            self.root = self._insert(self.root, value)
        else:
            return self._insert(node, value)


    def _insert(self, node, value):
        if not self.is_empty(node):

            if value < node.value:
                if node.left is not None:
                    self._insert(node.left, value)
                else:
                    node.left = Node(value)
            elif value > node.value:
                if node.right is not None:
                    self._insert(node.right, value)
                else:
                    node.right = Node(value)
        else:
            node = Node(value)

        return node


    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(f'{node.value}', sep=' ', end='')
            self.in_order(node.right)


    def pre_order(self, node):
        if node is not None:
            print(f'{node.value}', sep=' ', end='')
            self.pre_order(node.left)
            self.pre_order(node.right)


    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(f'{node.value}', sep=' ', end='')


    def showRoot(self):
        if self.root is None:
            print('A árvore está vazia!')
        print(f'Raiz: {self.root.value}')


    def remove_min(self, node):
        if node is None:
            print(' ERRO ')
        elif node.left is not None:
            node.left = self.remove_min(node.left)
            return node
        else:
            return node.right
        return None


    def find_min(self, node):
        if node is not None:
            while node.left is not None:
                node = node.left
        return node


    def remove(self, node, value):
        if node is None:
            print('A árvore está vazia!')
            return

        if value < node.value:
            node.left = self.remove(node.left, value)
        elif value > node.value:
            node.right = self.remove(node.right, value)
        elif node.left is not None and node.right is not None:
            node.value = self.find_min(node.right).value
            node.right = self.remove_min(node.right)
        else:
            node = node.left if node.left is None else node.right

        return node