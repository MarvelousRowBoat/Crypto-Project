from typing import List
import hashlib


class Node:
    def __init__(self, left, right, value):
        self.left: Node = left
        self.right: Node = right
        self.value = value

    @staticmethod
    def hash(val):
        return hashlib.sha256(val.encode('utf-8')).hexdigest()

    @staticmethod
    def doubleHash(val):
        return Node.hash(Node.hash(val))


class MerkleTree:
    def __init__(self, values: List[str]):
        self.__buildTree(values)

    def __buildTree(self, values: List[str]):
        leaves: List[Node] = [
            Node(None, None, Node.doubleHash(e)) for e in values]
        if len(leaves) % 2 == 1:
            # duplicate last elem if odd number of elements
            leaves.append(leaves[-1:][0])
        self.root: Node = self.__buildTreeRec(leaves)

    def __buildTreeRec(self, nodes: List[Node]):
        half: int = len(nodes) // 2

        if len(nodes) == 2:
            return Node(nodes[0], nodes[1], Node.doubleHash(nodes[0].value + nodes[1].value))

        left: Node = self.__buildTreeRec(nodes[:half])
        right: Node = self.__buildTreeRec(nodes[half:])
        value: str = Node.doubleHash(left.value + right.value)
        return Node(left, right, value)

    def printTree(self):
        self.__printTreeRec(self.root)

    def __printTreeRec(self, node):
        if node != None:
            print(node.value)
            self.__printTreeRec(node.left)
            self.__printTreeRec(node.right)

    def getRootHash(self):
        return self.root.value
