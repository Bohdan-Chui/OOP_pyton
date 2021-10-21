"""
    BINARY TREE that contains background information of product prices
    The tree is sorted by product codes.
"""
from Product import Product
from Node import Node


class BinaryTree:
    def __init__(self):
        self.node = None


    def add(self, product):
        if not isinstance(product, Product):
            raise TypeError('product must be Product type')
        if self.node is None:
            self.node = Node(product)
        else:
            self._addnode(product, self.node)

    def _addnode(self, product, node):
        if product.code < node.value.code:
            if node.left is not None:
                self._addnode(product, node.left)
            else:
                node.left = Node(product)
        else:
            if node.right is not None:
                self._addnode(product, node.right)
            else:
                node.right = Node(product)

    def find(self, code):
        if not isinstance(code, int):
            raise TypeError('input code')
        if self.node is not None:
            return self._find(code, self.node)
        else:
            return None

    def _find(self, code, node):
        if code == node.value.code:
            return node.value
        elif (code < node.value.code and node.left is not None):
            return self._find(code, node.left)
        elif (code > node.value.code and node.right is not None):
            return self._find(code, node.right)

    def printBinaryTree(self):
        if self.node is not None:
            self._printTree(self.node)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(node.value)
            self._printTree(node.right)
